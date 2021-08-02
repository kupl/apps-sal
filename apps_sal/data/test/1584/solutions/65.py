n = int(input())
L = list(map(int, input().split()))
L.sort()

ans = 0
for i, a in enumerate(L[2:]):
    k = i + 1
    for j, b in enumerate(L[:i + 2]):
        while j < k and a - b < L[k]:
            k -= 1
        ans += i - max(k, j) + 1

print(ans)
