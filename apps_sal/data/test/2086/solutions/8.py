n = int(input())
a = list(map(int, input().split()))
s, f = list(map(int, input().split()))

d = f - s
msum = 0
minx = 10**6
temp = a + a[:d + 1]
sumt = 0

for x in range(n + d + 1):
    sumt += temp[x]
    if (x >= d):
        sumt -= temp[x - d]
    #print(sumt, (n - x + s + d- 2)%n + 1, x)
    if (sumt > msum):
        minx = 10**6
        msum = sumt
        minx = min(minx, (n - x + s + d - 2) % n + 1)
    elif (sumt == msum):
        minx = min(minx, (n - x + s + d - 2) % n + 1)
print(minx)
