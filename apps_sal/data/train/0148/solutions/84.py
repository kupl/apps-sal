class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        dp_dict = dict(list(zip(difficulty, profit)))
        l = len(difficulty)
        for idx in range(l):
            d = difficulty[idx]
            if profit[idx] > dp_dict[d]:
                dp_dict[d] = profit[idx]
        dp_items = sorted(list(dp_dict.items()), key=lambda x: x[0])
        darr = [x[0] for x in dp_items]

        max_p = 0
        parr = list()
        for d, p in dp_items:
            if p > max_p:
                max_p = dp_dict[d]
            parr.append(max_p)

        ret = 0

        def get_nearest(w, arr):
            l = len(arr)
            if w < arr[0]:
                return None
            if w > arr[-1]:
                return l - 1

            def binary_search(w, i, j):
                if i >= l or j >= l or w < arr[i] or w > arr[j]:
                    return None
                if w == arr[i]:
                    return i
                if w == arr[j]:
                    return j
                k = (i + j) // 2
                if arr[k] <= w < arr[k + 1]:
                    return k
                prev = binary_search(w, i, k)
                return binary_search(w, k + 1, j) if prev is None else prev

            return binary_search(w, 0, l - 1)

        for w in worker:
            floor_idx = get_nearest(w, darr)
            if floor_idx is not None:
                ret += parr[floor_idx]
        return ret
