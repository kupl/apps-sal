"""

mountain = relative maximum
- find decr and incr after mountain

[2,1,4,7,3,2,5]

[2,3,2]


while j < len
    use flag to incr and decr
    
    while next and next incr
        j+=1
    
    if not incr:
        incr and cont
        
    while next and next decr
        j+=1
        
    if not decr:
        incr and cont
        
    if len 3
        check/override max
"""


class Solution:

    def longestMountain(self, A: List[int]) -> int:
        long_mont = 0
        (i, j) = (0, 0)
        while j < len(A):
            incr = False
            while j != len(A) - 1 and A[j] < A[j + 1]:
                incr = True
                j += 1
            if not incr:
                j += 1
                i = j
                continue
            decr = False
            while j != len(A) - 1 and A[j] > A[j + 1]:
                decr = True
                j += 1
            if not decr:
                j += 1
                i = j
                continue
            curr_len = j - i + 1
            if curr_len >= 3:
                long_mont = max(long_mont, curr_len)
            i = j
        return long_mont
