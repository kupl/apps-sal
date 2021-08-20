(n, k) = list(map(int, input().split()))
lis = list(map(int, input().split()))
ind = 0
for i in range(n):
    if lis[i] < 0:
        lis[i] *= -1
        k -= 1
        ind += 1
    elif lis[i] == 0:
        k = 0
        break
    else:
        break
    if k == 0:
        break
req = k % 2
if req:
    lis = sorted(lis)
    lis[0] = -1 * lis[0]
print(sum(lis))
