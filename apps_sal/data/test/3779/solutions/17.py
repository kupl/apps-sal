def gcd(a, b):
    if a < b:
        (a, b) = (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


(n, k) = list(map(int, input().split()))
l = list(map(int, input().split()))
gcdd = k
for i in range(n):
    gcdd = gcd(gcdd, l[i])
if gcdd == 0:
    print(1)
    print(0)
else:
    print(k // gcdd)
    ans = []
    for i in range(1, k // gcdd + 1):
        ans.append(i * gcdd % k)
print(' '.join(map(str, sorted(ans))))
