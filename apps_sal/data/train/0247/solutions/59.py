class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        '''
        1 1 1 2 2 3 1 1 1 1 1  target : 5
        '''
        
        sP = 0
        fP = 0
        
        intervalHeap = []
        sumSoFar = 0
        while fP < len(arr):
            sumSoFar += arr[fP]
            if sumSoFar >= target:
                if sumSoFar == target:
                    heapq.heappush(intervalHeap, (fP - sP + 1, sP, fP))
                    
                while sumSoFar >= target:
                    sumSoFar -= arr[sP]
                    sP += 1
                    if sumSoFar == target:
                        heapq.heappush(intervalHeap, (fP - sP + 1, sP, fP))
                
            fP += 1
        
        if len(intervalHeap) > 1:
            first = heapq.heappop(intervalHeap)
            second = heapq.heappop(intervalHeap)
            
            if first[2] < second[1] or second[2] < first[1]:
                return first[0] + second[0]
            else:
                while intervalHeap:
                    third = heapq.heappop(intervalHeap)
                    if third and first[2] < third[1] or third[2] < first[1]:
                        return first[0] + third[0]
                    elif third and second[2] < third[1] or third[2] < second[1]:
                        return second[0] + third[0]
        
        return -1

