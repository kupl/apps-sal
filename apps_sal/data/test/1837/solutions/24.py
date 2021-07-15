n = int(input())
a = [int(x) for x in input().split()]
ans = 0
flag = True
for i in range(n):
    if a[i] == i:
        ans += 1
    elif a[a[i]] == i and flag:
        ans += 2
        flag = False
if flag and ans < n:
    ans += 1
print(ans)
