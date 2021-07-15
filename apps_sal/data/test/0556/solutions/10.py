l, r, k = map(int, input().split())
ans = []
nowa = 1;
while (nowa <= r):
    if (nowa >= l):
        ans.append(nowa)
    nowa *= k
if (len(ans) == 0):
    print(-1)
else:
    print(*ans)
