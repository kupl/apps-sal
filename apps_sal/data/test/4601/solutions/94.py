(N, K) = map(int, input().split())
Hlist = list(map(int, input().split()))
if N - K > 0:
    print(sum(sorted(Hlist)[:N - K]))
else:
    print(0)
