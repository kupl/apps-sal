n = int(input())
l1 = list(map(int, input().split()))
l1.sort()
i = 0
ans = 0
while i < len(l1):
    if l1[i] >= ans + 1:
        i += 1
        ans += 1
    else:
        i += 1
print(ans)
