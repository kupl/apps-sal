n = int(input())
a = [*map(int, input().split())]
d = []
for i in range(min(a), max(a) + 1):
    temp = []
    for j in range(n):
        temp.append((a[j] - i)**2)
    d.append(sum(temp))
print(min(d))
