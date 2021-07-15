import itertools, math
n = int(input())
A = list(map(int, input().split()))
acc = [0] + list(itertools.accumulate(A))
ans = 0
seen = set()
for i in range(n - 2):
    a = int(math.log2(A[i]))
    for j in range(i + 2, n):
        cur = acc[j] - acc[i + 1]
        b = int(math.log2(cur))
        if b > a:
            break
        if A[i] ^ A[j] == cur and (i, j) not in seen:
            ans += 1
            seen.add((i, j))
for j in range(n - 1, 1, -1):
    a = int(math.log2(A[j]))
    for i in range(j - 2, -1, -1):
        cur = acc[j] - acc[i + 1]
        b = int(math.log2(cur))
        if b > a:
            break
        if A[i] ^ A[j] == cur and (i, j) not in seen:
            ans += 1
            seen.add((i, j))
print(ans)

