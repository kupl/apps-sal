def first(num):
    return num[0]


n, m = map(int, input().split())
num = list(map(int, input().split()))
lst = list(map(int, input().split()))
pr = []
for i in range(n):
    for j in range(m):
        pr.append([num[i] * lst[j], num[i], lst[j]])
pr.sort(key=first)
pr.reverse()
num.pop(num.index(pr[0][1]))
ans = -100000000000000000000000000000
for i in range(n - 1):
    for j in range(m):
        if num[i] * lst[j] > ans:
            ans = num[i] * lst[j]
print(ans)
