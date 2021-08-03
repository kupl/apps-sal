class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # BFS next step: +1, -1, same val pos
        # val_to_pos dict
        # dist dict

        if not arr:
            return 0

        n = len(arr)

        val_to_pos = collections.defaultdict(list)

        for i, val in enumerate(arr):
            val_to_pos[val].append(i)

        dist = 0

        curr_set = set([0])
        other_set = set([n - 1])

        curr_visited = curr_set
        other_visited = other_set

        while curr_set and other_set:
            if len(other_set) < len(curr_set):
                curr_set, other_set = other_set, curr_set
                curr_visited, other_visited = other_visited, curr_visited

            next_set = set()

            while curr_set:
                curr = curr_set.pop()

                if curr in other_visited:
                    return dist

                for nei in val_to_pos[arr[curr]] + [curr + 1, curr - 1]:
                    if not 0 <= nei < n:
                        continue

                    if nei in curr_visited:
                        continue

                    next_set.add(nei)

                val_to_pos[arr[curr]] = []

            curr_visited |= next_set
            curr_set = next_set
            dist += 1
