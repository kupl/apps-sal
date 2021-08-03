N, X = map(int, input().split())
L = list(map(int, input().split()))
ans = 1
total = 0
for l in L:
    total += l
    if total > X:
        break
    ans += 1
print(ans)
