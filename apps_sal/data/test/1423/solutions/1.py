n, l, r = map(int, input().split())
A = list(map(int, input().split()))
P = list(map(int, input().split()))
s = [0] * n
per = 0
for j in range(n):
    s[P[j] - 1] = j
b = [0] * n
b[s[0]] = l
for j in range(1, n):
    last = b[s[j - 1]] - A[s[j - 1]]
    nexs = last + 1

    if r - A[s[j]] > last:
        b[s[j]] = max(nexs + A[s[j]], l)
    else:
        per = 1
        break
if per == 1:
    print(-1)
else:
    print(' '.join(map(str, b)))
