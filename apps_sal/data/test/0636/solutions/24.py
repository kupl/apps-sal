line = input().split()

n = int(line[0])
k = int(line[1])

line = input().split()
lst = list()
for i in range(1, n + 1):
    lst.append((int(line[i - 1]), i))

lst.sort()
s = 0
c = 0
i = 0
ans = ''
while s < k and i < n:
    if s + lst[i][0] <= k:
        ans = ans + str(lst[i][1]) + ' '
        s += lst[i][0]
        c += 1
    else:
        break
    i += 1
print(str(c))
if c > 0:
    print(ans)
