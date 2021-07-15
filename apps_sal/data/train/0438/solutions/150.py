class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        ids = [i for i in range(n + 1)]
        weights = [0 for i in range(n + 1)]
        size_set = collections.defaultdict(int)
        ans = -1
        
        def find(i: int) -> int:
            while ids[i] != i:
                ids[i] = ids[ids[i]]
                i = ids[i]
            return i
        
        def union(i: int, j: int):
            i_id, j_id = find(i), find(j)
            i_weight, j_weight = weights[i_id], weights[j_id]
            new_weight = weights[i_id] + weights[j_id]
            if weights[i_id] > weights[j_id]:
                weights[i_id] = new_weight
                ids[j_id] = i_id
            else:
                weights[j_id] = new_weight
                ids[i_id] = j_id
            size_set[i_weight] -= 1
            size_set[j_weight] -= 1
            size_set[new_weight] += 1
        
        for i, index in enumerate(arr):
            weights[index] = 1
            size_set[1] += 1
            if index > 1:
                prev_id = find(index - 1)
                if weights[prev_id] > 0:
                    union(prev_id, index)
            if index < n:
                next_id = find(index + 1)
                if weights[next_id] > 0:
                    union(index, next_id)
            if size_set[m] > 0:
                ans = i + 1
        return ans
