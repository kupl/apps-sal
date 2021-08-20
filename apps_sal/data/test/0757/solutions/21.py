[n, m, k] = input().split()
n = int(n)
m = int(m)
k = int(k)
data = [int(i) for i in input().split()]
ans = 0
for i in reversed(sorted(data)):
    if k < m:
        k += int(i) - 1
        ans += 1
    else:
        break
if k < m:
    ans = -1
print(ans)
