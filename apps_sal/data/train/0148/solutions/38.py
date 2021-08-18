class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        val_dict = dict()
        for i in range(len(difficulty)):
            val_dict[difficulty[i]] = max(val_dict.get(difficulty[i], 0), profit[i])
        key_list = list(val_dict.keys())
        key_list = sorted(key_list)

        max_val = 0
        max_list = [0] * len(key_list)
        for i in range(len(key_list)):
            max_val = max(max_val, val_dict[key_list[i]])
            max_list[i] = max_val

        total = 0
        for w in worker:
            total += self.bisect(w, key_list, max_list)
        return total

    def bisect(self, w, key_list, max_list):

        left, right = 0, len(key_list) - 1
        if w < key_list[0]:
            return 0
        if w >= key_list[right]:
            return max_list[right]

        while left != right - 1:
            mid = (left + right) // 2
            if w > key_list[mid]:
                left = mid
            elif w < key_list[mid]:
                right = mid
            else:
                return max_list[mid]
        return max_list[left]
