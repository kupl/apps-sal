class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        ans = 0
        d = {}
        l = []
        res = 0
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in d:
            l.append(d[i])
        l.sort(reverse=True)
        print(l)
        for i in range(len(l)):
            res += l[i]
            if res >= (len(arr) // 2):
                return i + 1
