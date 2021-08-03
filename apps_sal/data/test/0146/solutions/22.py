n, k = list(map(int, input().split()))
t = list(map(int, input().split()))
sume = 0
sums = 0
ans = None
for i in range(n):
    if t[i] == 1:
        sume += 1
    else:
        sums += 1

for b in range(k):
    tsume = sume
    tsums = sums
    for i in range(b, n, k):
        if t[i] == 1:
            tsume -= 1
        else:
            tsums -= 1
    if ans == None:
        ans = abs(tsums - tsume)
    else:
        ans = max(ans, abs(tsums - tsume))
print(ans)
