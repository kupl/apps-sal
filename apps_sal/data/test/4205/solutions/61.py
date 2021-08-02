N = int(input())
p = list(map(int, input().split()))

# p_i != i なる要素p_iの数をkとするとき、
# k<=2 であるときに限り1回以下のスワップでpを昇順にできる
# k=0 のとき、最初からpは昇順
# k=1 にはならない
# k=2 のとき p_i != i である2つの要素を1回スワップすることでpを昇順にできる

q = list(range(1, N + 1))

k = 0
for i in range(N):
    if p[i] != q[i]: k += 1

if k <= 2: print('YES')
else: print('NO')
