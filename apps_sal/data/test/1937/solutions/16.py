n = int(input())
b = list(map(int, input().split()))
a = [0]
d = 0
for i in range(n//2-1):
    if b[i+1]>b[i]:
        d+=b[i+1] - b[i]
    a.append(d)
for i in range(n//2-1,-1,-1): a.append(b[i]-a[i])
print(' '.join(list(map(str,a))))
