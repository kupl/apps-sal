n, m, k = list(map(int, input().split()))
aa = list(map(int, input().split()))
bb = list(map(int, input().split()))
asum = [0]
bsum = [0]

for i in range(len(aa)):
    asum.append(asum[i] + aa[i])
for i in range(len(bb)):
    bsum.append(bsum[i] + bb[i])

j = len(bsum) - 1
ans = 0
for i in range(len(asum)):
    while j >= 0:
        if k >= asum[i] + bsum[j]:
            ans = max(ans, i + j)
            break
        else:
            j -= 1


print(ans)
