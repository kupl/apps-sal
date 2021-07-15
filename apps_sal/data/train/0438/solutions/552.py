class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        lookup = {}
        lastStep = -1
        valid = set()
        for idx, num in enumerate(arr):
            left = num
            right = num
            if num-1 in lookup:
                left = lookup[num-1][0]
                if num-1 in valid:
                    valid.remove(num-1)
                
            if num+1 in lookup:
                right = lookup[num+1][1]
                if num+1 in valid:
                    valid.remove(num+1)
            
            if left in valid:
                valid.remove(left)
            
            if right in valid:
                valid.remove(right)
                
            lookup[left] = (left, right)
            lookup[right] = (left, right)
            
            if right-left+1 == m:
                valid.add(left)
                valid.add(right)
            
            if valid:
                lastStep = idx+1
        return lastStep
