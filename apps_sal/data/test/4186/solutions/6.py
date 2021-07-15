MOD = 10**9 + 7
I = lambda:list(map(int,input().split()))

n, = I()
l = I()
l.sort()
count = 0
for i in range(0, n, 2):
    count += abs(l[i] - l[i+1])
print(count)
