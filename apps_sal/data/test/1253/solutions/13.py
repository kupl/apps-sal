(n, k) = list(map(int, input().split()))
lis = list(map(int, input().split()))
c = 0
for x in lis:
    if x < 0:
        c += 1
if c == n:
    for i in range(n):
        if k == 0:
            break
        k -= 1
        lis[i] = -lis[i]
    if k % 2 == 1:
        lis[n - 1] = -lis[n - 1]
elif c == 0:
    if k % 2 == 1:
        lis[0] = -lis[0]
else:
    i = 0
    while i in range(n):
        if lis[i] > 0 or k == 0:
            break
        k -= 1
        lis[i] = -lis[i]
        i += 1
    if k % 2 == 1:
        if lis[i] > lis[i - 1]:
            lis[i - 1] = -lis[i - 1]
        else:
            lis[i] = -lis[i]
print(sum(lis))
