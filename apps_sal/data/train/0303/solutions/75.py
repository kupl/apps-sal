import typing

class Solution:
    def maxSumAfterPartitioning(self, arr: typing.List[int], k: int) -> int:
        storage = {}
        def getSumRec(arr:list,i:int,k:int)->int:
            if i in storage:
                return storage[i]

            if not i<len(arr):
                return 0

            if len(arr) - i < k:
                return max(arr[i:])*len(arr[i:])

            listOfSums = []
            for offset in range(k):
                listOfSums.append( max(arr[i:i+offset+1] )*(offset+1) + getSumRec(arr,i+offset+1,k))

            storage[i] = max(listOfSums)
            return storage[i]

        return getSumRec(arr,0,k)
