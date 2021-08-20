(n, h) = map(int, input().split())
A = []
B = []
for i in range(n):
    (a, b) = map(int, input().split())
    A.append(a)
    B.append(b)
maxa = max(A)
C = []
B.sort(reverse=True)
ans = 0
for ele in B:
    if ele < maxa:
        break
    ans += 1
    h -= ele
    if h <= 0:
        break
if h > 0:
    ans += (h + maxa - 1) // maxa
print(ans)
