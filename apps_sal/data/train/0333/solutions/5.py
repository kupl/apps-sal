from collections import defaultdict


class Solution:
    def get_jump_indices(self, arr):
        jump_indices = defaultdict(set)
        for i, val in enumerate(arr):
            jump_indices[val].add(i)
        return jump_indices

    def minJumps(self, arr: List[int]) -> int:
        # Dictionary from array value to set of jumpable indices
        jump_indices = self.get_jump_indices(arr)
        next_indices = [len(arr) - 1]
        visited = set()
        visited.add(len(arr) - 1)
        jumps = 0
        while next_indices:
            reachable_indices_set = set()
            for index in next_indices:
                if index == 0:
                    return jumps
                reachable_indices = jump_indices[arr[index]].copy()
                reachable_indices.remove(index)
                reachable_indices.add(index - 1)
                if index != len(arr) - 1:
                    reachable_indices.add(index + 1)
                for reachable_index in reachable_indices:
                    if reachable_index in visited:
                        continue
                    visited.add(reachable_index)
                    reachable_indices_set.add(reachable_index)
            next_indices = list(reachable_indices_set)
            jumps += 1
        return None
