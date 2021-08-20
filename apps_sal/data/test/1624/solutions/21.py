n = int(input())
l = [*map(int, input().split())]
l.sort()
(i, j) = (0, n - 1)
res = 0
while i <= j:
    res += (l[i] + l[j]) ** 2
    i += 1
    j -= 1
print(res)
