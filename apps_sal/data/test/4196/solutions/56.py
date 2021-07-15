N = int(input())
a = list(map(int, input().split()))


def gcd(x, y):
    if x < y:
        x, y = y, x
    while y != 0:
        tmp = x % y
        x = y
        y = tmp
    return x


ans = 1
if N == 2:
    print(max(a))
    return

l = [1] * N
l[0] = a[0]
r = [1] * N
r[N-1] = a[N-1]
for i in range(1, N):
    l[i] = gcd(l[i-1], a[i])
    r[N-1-i] = gcd(r[N-i], a[N-1-i])
    
for i in range(N):
    if i == 0:
        n = r[1]
    elif i == N-1:
        n = l[N-2]
    else:
        n = gcd(l[i-1], r[i+1])
    ans = max(ans, n)
print(ans)
