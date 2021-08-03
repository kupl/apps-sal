
n = int(input())
a = list([int(x) for x in input().split(' ')])

a[1:] = sorted(enumerate(a[1:]), key=lambda x: x[1], reverse=1)
a[0] = (0, a[0])
for i in range(1, len(a)):
    a[i] = (a[i][0] + 1, a[i][1])

# print(a)

received = [0] * n
p = 1
pair = []

for i in range(n):
    #print(i >= p)
    if i >= p or p >= n:
        break
    #print('-', a[i][0])
    for j in range(a[i][1]):
        #print(p, a[p])
        pair.append((a[i][0], a[p][0]))
        p += 1
        if p == n:
            break

if p < n:
    print(-1)
else:
    print(str(len(pair)) + '\n' + str.join('\n', ['{} {}'.format(p[0] + 1, p[1] + 1) for p in pair]))


'''
4
1 2 1 0

6
2 0 1 3 2 0

6
2 3 2 0 1 0
'''

'''
3
1 0 0
'''
