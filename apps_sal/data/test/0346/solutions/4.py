(n, m) = list(map(int, input().split()))
lst = list(map(int, input().split()))
au = list(map(int, input().split()))
res = sum(lst)
ls = []
for i in range(m):
    res -= lst[au[i] - 1]
    ls.append(lst[au[i] - 1])
ls.sort(reverse=True)
for i in range(len(ls)):
    res += max(ls[i], res)
print(res)
