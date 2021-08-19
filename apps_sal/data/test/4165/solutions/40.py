a = [input().split() for l in range(2)]
N = int(a[0][0])
L = a[1]
sum = 0
for i in range(N):
    sum += int(L[i])
l_tf = []
for i in range(N):
    if 2 * int(L[i]) >= sum:
        print('No')
        break
else:
    print('Yes')
