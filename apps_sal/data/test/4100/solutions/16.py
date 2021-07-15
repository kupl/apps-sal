N, K, Q = map(int, input().split(' '))
rst = [ K for i in range(N) ]
for i in range(Q):
    A = int(input())
    rst[A - 1] += 1
for i in rst:
    if i - Q > 0:
        print('Yes')
    else:
        print('No')
