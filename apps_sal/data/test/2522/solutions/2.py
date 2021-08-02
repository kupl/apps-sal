# coding: utf-8
# Your code here!
import sys
readline = sys.stdin.readline
read = sys.stdin.read

n, = list(map(int, readline().split()))
*a, = list(map(int, readline().split()))
*b, = list(map(int, readline().split()))
b = b[::-1]

same = [i for i in range(n) if a[i] == b[i]]
if same:
    # 以下すべて半開区間
    v = a[same[0]]  # 重なる値は一種類しかない。これを v とおく。
    r = same[0]
    s = same[-1] + 1
    vidx = [i for i in range(n) if a[i] == v or b[i] == v]
    p = vidx[0]
    q = vidx[-1] + 1
    # [p,q) でかぶる。[r,s)でどちらかが値 v をとる
    if q > n - s + r + p:  # かぶりを吹っ飛ばせない
        print("No")
        return
    # かぶった部分を左、右によける
    if p >= s - r:
        b[r:s], b[:s - r] = b[:s - r], b[r:s]
    else:
        b[r:r + p], b[:p] = b[:p], b[r:r + p]
        b[r + p:s], b[n - s + r + p:] = b[n - s + r + p:], b[r + p:s]

print("Yes")
print((*b))
