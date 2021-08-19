class Solution:

    def minKBitFlips(self, A: List[int], K: int) -> int:
        """greedy+ 滑动窗口
        1.用deque保存反转过的idx，长度就是总共能管到i的反转次数
          start往后走的时候队头不在当前window的出站
          [0,0,0,1,0,1,1,0]
                         i
           que = [5]
           len == 1 => flipped  res += (len(que) %2 ^ A[i] == 0)
           res = 3
        2. 用count表示window里面flip了多少次(或者就用count的mod)
           flip的用A[i]-2 => 0:-2, 1:-1 来做mark这样start出window的时候才能减去count
           出window的时候把2加回去=> -2:0, -1:1
        """
        start = 0
        count = 0
        res = 0
        for (end, a) in enumerate(A):
            if count ^ A[end] == 0:
                A[end] -= 2
                res += 1
                count ^= 1
            if end >= start + K - 1:
                if A[start] < 0:
                    count ^= 1
                    A[start] += 2
                start += 1
        return -1 if any([a < 0 for a in A]) else res
