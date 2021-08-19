class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        hashMap = dict()
        for item in arr:
            if item not in hashMap:
                hashMap[item] = 0
            hashMap[item] += 1
        length = len(arr)
        itemToBeRemoved = 0
        halfOflength = len(arr) // 2
        for value in sorted(list(hashMap.values()), reverse=True):
            length -= value
            itemToBeRemoved += 1
            if length <= halfOflength:
                return itemToBeRemoved
