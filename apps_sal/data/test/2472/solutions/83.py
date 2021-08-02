n = int(input())
ba = []
for i in range(n):
    a, b = map(int, input().split())
    ba.append([b, a])
ba.sort()
t = 0
for i in range(n):
    t += ba[i][1]
    if t <= ba[i][0]:
        continue
    else:
        print('No')
        return
print('Yes')
