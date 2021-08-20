class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        val = [d[i] for i in d]
        val.sort(reverse=True)
        (count, total) = (0, 0)
        for each in val:
            total += each
            count += 1
            if total >= len(arr) // 2:
                break
        return count
