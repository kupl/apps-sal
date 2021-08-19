(n, x) = map(int, input().split())
list_m = list()
all = 0
for i in range(n):
    m = int(input())
    all += m
    list_m.append(m)
print(n + int((x - all) / min(list_m)))
