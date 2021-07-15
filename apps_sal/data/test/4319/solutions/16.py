n = int(input())
arr = map(int, input().split())
ans = {}
stairs = 0
for x in arr:
    if x == 1:
        stairs += 1
        ans[stairs] = 1
    else:
        ans[stairs] += 1
print(len(ans))
print(*ans.values())
