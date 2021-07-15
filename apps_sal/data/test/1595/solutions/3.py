sum, limit = map(int, input().split(' '))

ans = set()

def low_bit(n):
    k = 0
    while not n & (1 << k):
        k += 1
    return 1 << k

for i in reversed(range(1, limit + 1)):
    t = low_bit(i)
    if sum >= t:
        sum -= t
        ans.add(i)

if sum == 0:
    print(len(ans))
    print(' '.join([str(x) for x in ans]))
else:
    print(-1)
