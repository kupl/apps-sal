n = int(input())
a = list([int(x) for x in input().split(' ')])
a[1:] = sorted(enumerate(a[1:]), key=lambda x: x[1], reverse=1)
a[0] = (0, a[0])
for i in range(1, len(a)):
    a[i] = (a[i][0] + 1, a[i][1])
received = [0] * n
p = 1
pair = []
for i in range(n):
    if i >= p or p >= n:
        break
    for j in range(a[i][1]):
        pair.append((a[i][0], a[p][0]))
        p += 1
        if p == n:
            break
if p < n:
    print(-1)
else:
    print(str(len(pair)) + '\n' + str.join('\n', ['{} {}'.format(p[0] + 1, p[1] + 1) for p in pair]))
'\n4\n1 2 1 0\n\n6\n2 0 1 3 2 0\n\n6\n2 3 2 0 1 0\n'
'\n3\n1 0 0\n'
