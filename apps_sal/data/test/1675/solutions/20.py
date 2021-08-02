n = int(input())
i = 0
l1 = list()
l2 = list()
l3 = [0] + [0] * 10**5
l4 = [0] + [0] * 10**5
i = 0
while i < n:
    x, y = list(map(int, input().split()))
    l1.append(x)
    l2.append(y)
    l3[x] += 1
    l4[y] += 1
    i += 1

i = 0
for i in range(n):
    print(n - 1 + l3[l2[i]], n - 1 - l3[l2[i]])
