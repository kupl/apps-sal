N = int(input())
x = list(map(int, input().split()))
f = min(x)
ans = N * f
curlen = 0
maxlen = 0
index = 0
while index < 2 * N:
    if x[index % N] == f:
        maxlen = max(maxlen, curlen)
        curlen = 0
    else:
        curlen += 1
    index += 1
maxlen = max(maxlen, curlen)
print(ans + maxlen)
