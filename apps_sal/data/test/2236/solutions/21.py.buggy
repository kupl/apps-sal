n = int(input())
a = list(map(int, input().split()))
if a == [0] * n:
    print(0)
    return
dp1 = [0] * (n)
dp1[0] = a[0]
for i in range(1, n):
    dp1[i] = dp1[i - 1] + a[i]
res = 0
counter = {}
for i in range(n):
    try:
        counter[dp1[i]] += 1
    except:
        counter[dp1[i]] = 1
for elem in counter:
    res = max(res, counter[elem])
print(n - res)
