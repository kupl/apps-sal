class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # intuitive idea: for current position, if it flips, 
        # then we record the right-hand-side farest point that current flip will effect to (whick is i+K-1)
        # call this 'forward propogation'
        # on the other hand, at current position, we need to decite whether we need to flip it or not,
        # this time, we need to look at \"backward propogation\": 
        # the flips that happended historically and still effect current i-th position:
        # 1. if there are even flips effect current i, then when A[i]=0, we need a new flip
        # 2. if there are odd flips effect current i, then only when A[i]=1, we need a new flip
        # when we perform this flip, we will append a new right-hand-side boundary (i+K-1) to current queue:

        # time complexity = O(n) and space complexity = O(K)
        flips = collections.deque() # alike a sliding window, that store the active flips 
        # (which effect current i-th position)

        res = 0
        for i in range(len(A)):
            if A[i] == (len(flips) % 2):
                res += 1
                flips.append(i+K-1)

            if flips and flips[0] <= i: # the head of the queue will not effect i+1 th position, so we pop it
                flips.popleft()
        return res if not flips else -1

