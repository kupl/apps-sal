n, m, k = list(map(int, input().split()))
aArr = list(map(int, input().split()))
bArr = list(map(int, input().split()))

t = sum(bArr)
ans = 0
j = m

for i in range(n + 1):
    while j > 0 and t > k:
        j -= 1
        t -= bArr[j]
    if t > k:
        break
    ans = max(ans, i + j)
    if i == n:
        break
    t += aArr[i]

print(ans)
