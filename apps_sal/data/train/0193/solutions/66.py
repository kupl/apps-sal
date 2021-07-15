class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        result = list()
        count = 0
        for k,v in sorted(c.items(),key = lambda item: item[1],reverse=True):
            if count < len(arr)//2:
                result.append(k)
                count += v
        return len(result)
