n = int(input())
a = list(map(int, input().split()))
s = list()
for i in range(n-1):
    s.append(a[i+1] - a[i])
diff = max(s)
minsum = 10000
for i in range(0, len(s)-1):
    if s[i]+s[i+1] < minsum:
        minsum = s[i]+s[i+1]
if minsum > diff:
    print(minsum)
else:
    print(diff)
