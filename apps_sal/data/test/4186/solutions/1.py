input()
l = list(map(int, input().split()))
l.sort()
n = 0
for x in range(len(l) // 2):
    n += l[x * 2 + 1] - l[x * 2]
print(n)
