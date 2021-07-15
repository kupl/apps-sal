n, p = map(int, input().split())
A = []
for i in range(n):
    s = input()
    A.append(2 if s == 'half' else 1)

A.pop()
A = A[::-1]

h = p // 2
ans = h
c = 1
for i in range(n - 1):
    if A[i] == 1:
        ans += p * c + h
        c = c * 2 + 1 
    else:
        ans += c * p
        c *= 2
print(ans)
