class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        dic = Counter(arr)
        h = [(val*(-1),key) for key,val in list(dic.items())]
        heapify(h)
        #print(h)
        seen = set()
        count = 0
        while 2*count*(-1) < len(arr):
            c,i = heappop(h)
            count += c
            seen.add(i)
            #print(seen)
        return len(seen)

