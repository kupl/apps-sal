N = int(input())
a = list(map(int, input().split()))
avg = round(sum(a)/N)
sums = []
for i in range(min(a), avg+1):
    s = 0
    for j in range(N):
        s += (i-a[j])**2
    sums.append(s)
print(min(sums))
