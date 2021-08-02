n = int(input())
a = list(map(int, input().split()))

dic = {}

ans = 0
for i in range(n):
    if i + 1 - a[i] in dic:
        ans += dic[i + 1 - a[i]]

    if a[i] + (i + 1) in dic:
        dic[(i + 1) + a[i]] = dic[(i + 1) + a[i]] + 1
    else:
        dic[(i + 1) + a[i]] = 1

print(ans)
