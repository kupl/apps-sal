class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hash_map = collections.Counter(arr)
        hash_map = {k:v for k,v in sorted(hash_map.items(),key=lambda item: item[1])}
        total_size = len(arr)
        values = list(hash_map.values())[::-1]
        # print(values)
        ans=0
        i=0
        while total_size>len(arr)//2:
            total_size-=values[i]
            i+=1
            ans+=1
        return ans
