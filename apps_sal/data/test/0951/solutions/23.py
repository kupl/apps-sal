k = int(input())
n = list(map(int, list(input().strip())))
n.sort()
s = sum(n)
c = 0
i = 0
while s < k:
    s += 9 - n[i]
    i += 1
    c += 1
print(c)
