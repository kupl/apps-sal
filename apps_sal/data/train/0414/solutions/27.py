from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # winner remains at position 0
        # loser moves to end of array
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

#         if len(arr) < 3:
#             return min(arr)


#         q = deque(arr[::-1])
#         # append on right
#         # dequeue on left
#         count = 0
#         while(count < k):
#             comp1, comp2 = arr[-1], arr[-2]
#             #   if new winner
#             if comp2 > comp1:
#                 arr.append(arr.pop())
#                 count = 1
#             else:
#             # if current winner
#                 arr[-1] = comp2
#                 arr[-2] = comp1
#                 arr.append(arr.pop())
#                 count += 1

#         return arr[-1]

        count = 0
    #     [2,1,3]
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


#     i need to know how many  smaller elements there will be after each
# sort? keep track of sorted indices?
# i only care about what's immediately before it, and next term that is largest
# after first round, it's sorted in asc order - if it doesn't win the first itme it appears, it won't win
# idea - for each - keep number which are greater than it k*n
# idea - sort all (nlogn) and for each, check how many after it are less than it;
# if a bigger number comes before a smaller one and will win, it will win for sure
# if a smaller numnber comes before a bigger number, if it hasn't won it won't win
    # if k < sz this is fine
    # otherwise
    # if we get to the end, the largest number is the winner
