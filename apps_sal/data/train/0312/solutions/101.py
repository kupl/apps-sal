class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        # algorihtm
        # find the minimum length of the subarray, where there sum >= k
        # when dealing sum, sum prifix?
        
        # sliding window -classis?  O(N^2)
        # holding a deque ?yes
        #   decreasing or increasing?
        #   decresaing? X    no need to save the one before  ==> choose increasing
        #   save number or index??? we need to i - index, so save index in deque
        #   when add / delete our dequeue: 
        #          add ==> in for loop
        #          delete ==> sum_[i] <= sum_[queue[-1]], pop()
        #                     sum_[i] - sum_[deque[0]] >= K, pop(0)
        
        # deque
        sum_ = [0]
        for num in A:
            sum_.append(sum_[-1] + num)
        result = len(A)+1
        deque = []
        for i,num in enumerate(sum_):
            while(deque and num <= sum_[deque[-1]]):
                deque.pop()
            while(deque and num - sum_[deque[0]] >= K):
                result = min(result, i - deque[0])
                deque.pop(0)
            deque.append(i)
                
        return result if result != len(A)+1 else -1
        



