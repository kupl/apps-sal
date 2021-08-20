n = int(input())
lst = list(map(int, input().split()))
lst.sort()
M = lst[-1]
m = lst[0]
total = float('inf')
for i in range(m, M + 1):
    s = sum([(x - i) ** 2 for x in lst])
    if s < total:
        total = s
print(total)
