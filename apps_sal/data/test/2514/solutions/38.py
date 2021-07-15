from collections import Counter
n = int(input())
A = list(map(int, input().split()))
C = Counter(A)
q = int(input())
ans = sum(A)
for _ in range(q):
    b, c = list(map(int, input().split()))
    if C.get(b):
        x = C.pop(b)
        ans += - b * x + c * x
        if C.get(c):
            C[c] += x
        else:
            C[c] = x
    print(ans)

