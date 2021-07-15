s, p = map(int, input().split(' '))

for n in range(1, s):
    m = s - n
    if m * n == p:
        print('Yes')
        return
    if m * n > p:
        break
print('No')
