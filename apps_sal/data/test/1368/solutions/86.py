import math
(n, a, b) = map(int, input().split())
V = list(map(int, input().split()))
V.sort(reverse=True)


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


ans = 0
x = 0
y = 0
for i in range(n):
    if i <= a - 1:
        ans += V[i]
        if V[i] == V[a - 1]:
            x += 1
            y += 1
    elif V[i] == V[a - 1]:
        x += 1
if V[0] != V[a - 1]:
    cnt = combinations_count(x, y)
    print(ans / a)
    print(cnt)
else:
    cnt = 0
    for i in range(a, b + 1):
        if i <= x:
            cnt += combinations_count(x, i)
    print(ans / a)
    print(cnt)
