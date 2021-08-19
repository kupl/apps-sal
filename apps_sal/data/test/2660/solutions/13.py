import heapq
Q = int(input())

# 中央値の左側の値、右側の値を管理する
# heapqとする。rightは最小が興味あるが、leftは最大なので、-1をかけて扱う
left, right = [], []
# 両方のSUMも管理する必要がある。毎回SUMしてたら間に合わん
Lsum, Rsum = 0, 0
Lcnt, Rcnt = 0, 0
B = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if len(q) == 1:
        # 2
        # heapqってPeakできないの・・・？
        l = (-1) * heapq.heappop(left)
        heapq.heappush(left, (-1) * l)
        # (l-l1) + (l-l2) + ... + (l-l) + (r-l) + ... + (r1 - l)
        print(l, Rsum // 2 - Lsum // 2 + B)
        #print(left,right, Lsum, Rsum)
    else:
        # 1
        _, a, b = q
        B += b
        # まず双方にaを突っ込む
        heapq.heappush(left, (-1) * a)
        heapq.heappush(right, a)
        Lsum += a
        Lcnt += 1
        Rsum += a
        Rcnt += 1
        # leftの最大値と、rightの最小値の関係が崩れていたら、交換する
        l = (-1) * heapq.heappop(left)
        r = heapq.heappop(right)
        if l >= r:
            Lsum = Lsum - l + r
            Rsum = Rsum - r + l
            l, r = r, l
        heapq.heappush(left, (-1) * l)
        heapq.heappush(right, r)
