class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic=collections.defaultdict(int)
        for i in range(len(arr)):
            dic[arr[i]]+=1
        num=[]
        total=0
        for key in list(dic.keys()):
            num.append(dic[key])
            total+=1
        num.sort()
        count=0
        while(k>0 and num):
            k-=num[0]
            num.pop(0)
            if k<0:
                break
            count+=1
        return total-count
        

