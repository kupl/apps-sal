# You lost the game.

n, n1, n2 = list(map(int, input().split()))
L = list(map(int, input().split()))

L.sort(reverse=True)

L1 = L[:n1]
L2 = L[n1:n1 + n2]

L3 = L[:n2]
L4 = L[n2:n1 + n2]

r1 = sum(L1) / n1 + sum(L2) / n2
r2 = sum(L3) / n2 + sum(L4) / n1

print(max(r1, r2))
