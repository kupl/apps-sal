n = int(input())
data = list(map(int, input().split()))
sums = [data[0]]
ans = 0
if sums[0] > 100:
    ans = 1
    
for i in range(1, n):
    ns = sums[-1] + data[i]
    sums += [ns]
    if ns > (i + 1) * 100:
        ans = i + 1
        
for i in range(1, n):
    for j in range(i + ans, n):
        if sums[j] - sums[i - 1] > (j - i + 1) * 100:
            ans = j - i + 1

print(ans)
