class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # corner case
        if len(arr) == 1:
            return 0

        # create a better lookup data structure
        dict_ = collections.defaultdict(list)
        for index in range(len(arr)):
            dict_[arr[index]].append(index)

        # print(dict_)

        # a variable to save ans
        min_count = 0

        # remember visited points
        visited = set()
        visited.add((arr[0], 0))

        # bfs
        queue = collections.deque()
        queue.append((arr[0], 0))

        while queue:
            # print(queue)
            size = len(queue)
            # spread the nodes at the same level
            for i in range(size):
                curr_num, index = queue.popleft()
                # print(\"index: \",index)
                # reach the condition
                if index == len(arr) - 1:
                    return min_count
                # add unvisited neighbor points to the queue
                for new_num, new_index in self.move(curr_num, index, arr, dict_, visited):
                    if (new_num, new_index) not in visited:
                        # print(\"new_index: \", new_index)
                        visited.add((new_num, new_index))
                        queue.append((new_num, new_index))
            min_count = min_count + 1

    def move(self, curr_num, index, arr, dict_, visited):
        for new_num, new_index in [(arr[index - 1], index - 1), (arr[index + 1], index + 1)]:
            if 0 <= new_index < len(arr) and (new_num, new_index) not in visited:
                yield new_num, new_index
        if dict_[curr_num]:
            new_num = curr_num
            for new_index in dict_[curr_num]:
                if 0 <= new_index < len(arr) and (new_num, new_index) not in visited:
                    yield new_num, new_index
            del dict_[curr_num]
