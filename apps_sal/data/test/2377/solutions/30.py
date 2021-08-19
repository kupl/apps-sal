(n, h) = list(map(int, input().split()))
A = []
B = []
for i in range(n):
    (a, b) = list(map(int, input().split()))
    A.append(a)
    B.append(b)
A.sort(reverse=True)
B.sort(reverse=True)
B = [i for i in B if i > A[0]]
ans = 0
for i in B:
    ans += 1
    h -= i
    if h <= 0:
        break
if h > 0:
    if h % A[0] == 0:
        ans += h // A[0]
    else:
        ans += h // A[0] + 1
print(ans)
