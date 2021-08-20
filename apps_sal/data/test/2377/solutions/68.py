(n, h) = map(int, input().split())
(A, B) = ([0] * n, [0] * n)
for i in range(n):
    (A[i], B[i]) = map(int, input().split())
A_max = max(A)
B.sort(reverse=True)
ans = 0
for i in B:
    if i > A_max:
        h -= i
        ans += 1
        if h <= 0:
            h = 0
            break
    else:
        break
if h < 0:
    h = 0
q = h / A_max
p = q % 1
ans += int(q)
if p > 0:
    print(ans + 1)
else:
    print(ans)
