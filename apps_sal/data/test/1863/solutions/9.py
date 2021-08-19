n = int(input())
l = ['A'] * n
p = 0
for i in range(n):
    a = int(input().split()[0])
    if p + a <= 500:
        p += a
    else:
        p -= 1000 - a
        l[i] = 'G'
print(''.join(l))
