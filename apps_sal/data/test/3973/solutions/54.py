import sys
input = sys.stdin.readline
n, m = map(int,input().split())
A = list(map(int,input().split()))
for i in range(n):
    A[i] -= 1

class Bit:  # Fenwick Tree と同じ
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
  
    def sum(self, l, r):  # [l,r)の和を求める
        # 内部的には[l+1,r+1)の和つまり(rまでの和-lまでの和)
        s = 0
        while r > 0:
            s += self.tree[r]
            r -= r & -r  # 2進数の最も下位の1を取り除くという意味(例:1010→1000)
        while l > 0:
            s -= self.tree[l]
            l -= l & -l  # 2進数の最も下位の1を取り除くという意味(例:1010→1000)
        return s
  
    def add(self, i, x):  # i番目にxを足す
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i  # 2進数の最も下位の1を繰り上げるという意味(例:1010→1100)

    def sett(self, i, x):  # i番目をxにする
        self.add(i, x - self.sum(i, i+1))

    def print_bit(self): # 内部状態をindex順に出力
        print([self.sum(i, i+1) for i in range(self.size)])

    def print_sum(self): # 累積和をindex順に出力
        print([self.sum(0, i+1) for i in range(self.size)])

    def lower_bound_left(self, w):  # xまでの和がw以上となる最小のx、総和がw未満の場合nが返る
        n = self.size
        r = 1
        x = 0
        if self.sum(0, n) < w:
            return n
        while r < n:
            r *= 2
        le = r
        while le > 0:
            if (x + le < n and self.tree[x+le] < w):
                w -= self.tree[x+le]
                x += le
            le //= 2
        return x

    def upper_bound_left(self, w):  # xまでの和がwより大きくなる最小のx、総和がw以下の場合nが返る
        n = self.size
        r = 1
        x = 0
        if self.sum(0, n) <= w:
            return n
        while r < n:
            r *= 2
        le = r
        while le > 0:
            if (x + le < n and self.tree[x+le] <= w):
                w -= self.tree[x+le]
                x += le
            le //= 2
        return x

    def lower_bound_right(self, w):  # xまでの和がw以下となる最大のx、0番目がwより大きい場合-1が返る
        return self.upper_bound_left(w) - 1

    def upper_bound_right(self, w):  # xまでの和がw未満となる最大のx、0番目がw以上の場合-1が返る
        return self.lower_bound_left(w) - 1

B = Bit(m*3)

for i in range(n-1):
    a = A[i]
    b = A[i+1]
    if a == b:
        continue
    d = (b-a) % m
    ra = d - 1
    l1 = a + 2
    r1 = l1 + ra
    B.add(l1, 1)
    B.add(r1, -1)
    B.add(r1, -ra)
    B.add(r1+1, ra)
    # lm1 = r1
    # rm1 = min(r1 + ra, a + m + 1)
    # B.add(lm1, -1)
    # B.add(rm1, 1)
    # p = (r1-l1) - (rm1-lm1)
    # print("p",p)
    # if p > 0:
    #     B.add(rm1-1, -p)
    #     B.add(rm1, p)
    # B.print_sum()

S = [B.sum(0, i+1) for i in range(3*m)]
for i in range(1, 3*m):
    S[i] += S[i-1]

# print(S)

ANS = [0] * m
for i in range(3*m):
    ANS[i%m] += S[i]

now = 0
for i in range(n-1):
    now += (A[i+1]-A[i]) % m

print(now - max(ANS))    
