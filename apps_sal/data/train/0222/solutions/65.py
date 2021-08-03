class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        exists = set(A)
        max_length = 2

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a = A[i]
                b = A[j]
                curr_length = 2

                while (a + b) in exists:
                    curr_length += 1
                    #curr = a + b
                    #a = b
                    #b = curr
                    a, b = b, a + b
                max_length = max(max_length, curr_length)

        if max_length <= 2:
            return 0
        return max_length


# [1,2,3,4,5,6,7,8]
#
# **** START == 1 ****
#
# second = 1
# first = 2
# curr_length = 3
# curr = 3

# cache[1] = max(cache[1]+1, 3)
# cache[1] = max(0+1, 3)
# cache[1] = 3
#
# second = 2
# first = 3
# curr_length = 4
# curr = 5
#
# cache[1] = max(cache[1], curr_length)
# cache[1] = max(3, 3)
# cache[1] = 4
#
# second = 3
# first = 5
# curr_length = 5
# curr = 8
#
# cache[1] = max(cache[1], 5)
# cache[1] = 5
#
# second = 5
# first = 8
# curr_length = 6
# curr = 13
#
# 13 not in A, next pair
#
#
# **** START == 1 ****
#
# second = 1
# first = 3
# curr_length = 3
# curr = 4
#
# cache[1] = max(5, 3)
# cache[1] = 5
#
# second = 3
# first = 4
# curr = 7
# curr_length = 4
#
# cache[1] = max(5, 4)
# cache[1] = 5
#
# second = 4
# first = 7
# curr = 11
#
# 11 not in A, exit
#
