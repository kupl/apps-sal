(n, k) = list(map(int, input().split()))
L = list(map(str, input().split()))
ans = 0
for l in L:
    if l.count('4') + l.count('7') <= k:
        ans += 1
print(ans)
