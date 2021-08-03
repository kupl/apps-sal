n = int(input())
a = list(map(int, input().split()))
m = min(a)
b = [int(a[i] > m) for i in range(n)]
L = Max = 0
last = -1
for i in range(n):
    if b[i] == 0 and last != -1:
        Max = max(i - last, Max)
        last = -1
    elif last == -1 and b[i]:
        last = i
if last != -1:
    Max = max(n - last, Max)
if b[0] and b[-1]:
    L = 0
    R = n - 1
    while b[L] and L < n - 1:
        L += 1
    while b[R] and L > 0:
        R -= 1
    L -= 1
    R += 1
    Max = max(L + n - R + 1, Max)
ans = m * n + Max
print(ans)
