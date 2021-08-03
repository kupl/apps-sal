n = int(input())
L = list(map(int, input().split()))
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a = L[i]
            b = L[j]
            c = L[k]
            A = [a, b, c]
            if a == b or b == c or c == a:
                continue
            if sum(A) - 2 * max(A) > 0:
                ans += 1
print(ans)
