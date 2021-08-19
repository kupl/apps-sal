N = int(input())
A = list(map(int, input().split()))
target = 1
ans = 0
for a in A:
    if a == target:
        target += 1
    else:
        ans += 1
print(ans if target != 1 else -1)
