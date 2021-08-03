n = int(input())

tot = sum(map(int, input().split()))

m = int(input())

P = []
for i in range(m):
    l, r = list(map(int, input().split()))
    P.append((l, r))

for l, r in P:
    if (l <= tot and tot <= r):
        print(tot)
        return
    elif (tot <= l):
        print(l)
        return

print(-1)
