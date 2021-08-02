N, K = map(int, input().split())
A = list(map(int, input().split()))
l = 0
r = 10**9
while (r - l > 1):
    x = (r + l) // 2
    now = 0
    for a in A:
        now += (a - 1) // x
    if now <= K:
        r = x
    else:
        l = x
print(r)
