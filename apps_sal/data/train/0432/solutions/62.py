class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        #hashmap count
        countMap = {}
        for num in nums:
            countMap[num] = countMap.get(num,0) + 1     
        #sort keys
        keyList = list(countMap.keys())
        keyList.sort()

        while len(keyList) >0:
            print(keyList)
            if len(keyList) < k:
                return False
            remove = []
            for i in range (k):
                if i > 0 and (keyList[i] - keyList[i-1] > 1):
                    return False
                #update map and maybe list
                countMap[keyList[i]] = countMap[keyList[i]] -1
                if countMap[keyList[i]] == 0:
                    remove.append(keyList[i])
            for key in remove:
                keyList.remove(key)
        return True
        
        
        #pull lowest k, update counts and key sorted 

