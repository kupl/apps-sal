n, m = map(int, input().split())
num = []
for i in range(n):
    l, r = map(int, input().split())
    num.append([l, r])
ans = []
for i in range(1, m + 1):
    for j in range(n):
        if num[j][0] <= i and num[j][1] >= i:
            break
    else:
        ans.append(i)
print(len(ans))
if ans:
    print(*ans)
