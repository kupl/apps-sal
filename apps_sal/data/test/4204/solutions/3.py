s = list(map(str, input().rstrip()))
k = int(input())
ans = 1
for x in s[:k]:
    if int(x) != 1:
        ans = int(x)
        break
print(ans)
