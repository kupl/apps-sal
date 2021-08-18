class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        dict_ = collections.defaultdict(list)
        for index in range(len(arr)):
            dict_[arr[index]].append(index)

        min_count = 0

        visited = set()
        visited.add((arr[0], 0))

        queue = collections.deque()
        queue.append((arr[0], 0))

        while queue:
            size = len(queue)
            for i in range(size):
                curr_num, index = queue.popleft()
                if index == len(arr) - 1:
                    return min_count
                for new_num, new_index in self.move(curr_num, index, arr, dict_, visited):
                    if (new_num, new_index) not in visited:
                        visited.add((new_num, new_index))
                        queue.append((new_num, new_index))
            min_count = min_count + 1

    def move(self, curr_num, index, arr, dict_, visited):
        for new_num, new_index in [(arr[index - 1], index - 1), (arr[index + 1], index + 1)]:
            if 0 <= new_index < len(arr):
                yield new_num, new_index
        if dict_[curr_num]:
            for new_index in dict_[curr_num]:
                new_num = curr_num
                if 0 <= new_index < len(arr) and (new_num, new_index) not in visited:
                    yield new_num, new_index
            del dict_[curr_num]
