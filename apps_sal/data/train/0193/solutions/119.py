class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        d = sorted(d.items(), key = lambda x:x[1], reverse=True)
        print(d)
        total, count = 0, 0
        for i in d:
            total += i[1]
            count+=1
            if total >= len(arr)//2:
                return count
