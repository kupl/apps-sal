class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        l = len(arr)
        s = 0

        cnt = Counter(arr)
        cnt = [j for i, j in cnt.items()]
        cnt.sort(reverse=True)
        for ind, i in enumerate(cnt):
            s += i
            if s >= l // 2:
                break
        return ind + 1
