(n, t) = map(int, input().split())
lst = list(map(int, input().split())) + [10 ** 12]
sec = 0
for i in range(n):
    sec += min(t, lst[i + 1] - lst[i])
print(sec)
