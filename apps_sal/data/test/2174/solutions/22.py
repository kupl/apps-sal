n = int(input())
a = [int(x) for x in input().split()]
a.sort()
res = 0
for i in range(len(a)):
    res += abs(i + 1 - a[i])
print(res)
