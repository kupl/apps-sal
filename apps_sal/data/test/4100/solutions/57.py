N, K, Q = map(int, input().split(' '))
ls = [K for i in range(N)]
for i in range(Q):
    A = int(input())
    ls[A - 1] += 1
for i in ls:
    if i - Q > 0:
        print('Yes')
    else:
        print('No')
