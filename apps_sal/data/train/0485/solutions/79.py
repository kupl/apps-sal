class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # to maintain a queue to record the position where flip happens in the k window that ends at the current position
        win = collections.deque()
        ans = 0
        for i,x in enumerate(A):
            while len(win)>0 and win[0]<i-K+1:
                win.popleft()
            if (x ^ (len(win)%2) ) ==0  :  # if there are even number of flips and x == 0, need to flip, odd and x==1
                if i+K-1<=len(A)-1:
                    ans += 1
                    win.append(i)
                else:
                    return -1
        return ans
