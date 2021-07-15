n, k = map(int, input().split())
ppp = list(map(int, input().split()))
ppp.sort()
print(sum(ppp[:k]))
