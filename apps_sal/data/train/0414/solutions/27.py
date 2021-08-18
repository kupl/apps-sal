from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        '''
        arr = [2,1,3,5,4,6,7]
        k = 2 

        [2,3,5,4,6,7,1]
        [3,5,4,6,7,1,2]
        [5,4,]

        question - if no rotation - first number
        1) indicator that number geq than prev number
        2) consecutive numbers greater than 
        is >= k

        otherwise 
        1) same - with each integer at beginning; count the sum of consecutive elements it's greater than from index [i - 1], [min(len(i) - 1,i + k)]

        otherwise 
        1) if len is less than (k), then we have to loop through; 

        any better way of doing this?
        this way will be O(k*n) - constant

        question - what's the best way to shift array? (pop? append)
        queue? i need to remove either top or second top element
        swap first and second, dequeue 

        '''

        count = 0
        current = arr[0]
        for i in range(1, len(arr)):
            if count >= k:
                return current
            elif arr[i] > current:
                current = arr[i]
                count = 1
            else:
                count += 1
        return current
