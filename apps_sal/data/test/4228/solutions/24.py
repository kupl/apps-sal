(N, L) = list(map(int, input().split()))
flavor = []
flavorabs = []
for i in range(1, N + 1):
    flavor.append(L + i - 1)
S = 0
for i in flavor:
    S += i
for i in range(N):
    flavorabs.append(abs(flavor[i]))
a = min(flavorabs)
print(S - flavor[flavorabs.index(a)])
