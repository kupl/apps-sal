x = int(input())
l = [0] + list(map(int, input().split(' ')))
m = 10 ** 9
ind = 0
for i in range(1, 10):
    if l[i] <= m:
        m = l[i]
        ind = i
if m > x:
    print(-1)
    quit()
dig = x // m
k = [ind] * dig
left = x - dig * m
for i in range(dig):
    for j in range(9, 0, -1):
        diff = l[j] - l[k[i]]
        if diff <= left:
            left -= diff
            k[i] = str(j)
            break
    k[i] = str(k[i])
print(''.join(k))
