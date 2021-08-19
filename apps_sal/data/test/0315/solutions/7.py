s = input().split(' ')
n = int(s[0])
k = int(s[1])
d = [int(x) for x in input().split(' ')]
over = 0
for i in range(n - 1):
    need = k - d[i + 1]
    if need <= 0:
        continue
    need -= d[i]
    if need > 0:
        d[i + 1] += need
        over += need
print(over)
print(' '.join([str(x) for x in d]))
