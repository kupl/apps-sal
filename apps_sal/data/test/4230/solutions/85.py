X, N = list(map(int, input().split()))
pi = list(map(int, input().split()))

mind = 10**10
ans = -102
for i in range(-101, 102):
    dist = abs(X - i)
    if mind > dist:
        if i not in pi:
            ans = i
            mind = dist


print(ans)

