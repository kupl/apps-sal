N, K, Q = map(int, input().split(' '))
val = [ K for i in range(N) ]
for i in range(Q):
    A = int(input())
    val[A - 1] += 1
for i in val:
    if i - Q > 0:
        print('Yes')
    else:
        print('No')
