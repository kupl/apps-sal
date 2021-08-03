
class Solution:
    def minSetSize(self, array: List[int]) -> int:
        hashMap = dict()
        for item in array:
            if item not in hashMap:
                hashMap[item] = 0
            hashMap[item] += 1

        length = len(array)
        itemToBeRemoved = 0
        halfOflength = len(array) // 2

        for value in sorted(list(hashMap.values()), reverse=True):
            length -= value
            itemToBeRemoved += 1
            if length <= halfOflength:
                return itemToBeRemoved
