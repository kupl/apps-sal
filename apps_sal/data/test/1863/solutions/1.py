n = int(input())
l = ['A'] * n
p = 500
for i in range(n):
    a = int(input().split()[0])
    if 0 <= p + a <= 1000:
        p += a
    else:
        l[i] = 'G'
        p -= 1000 - a
print(''.join(l))
