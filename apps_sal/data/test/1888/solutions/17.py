from sys import stdin
(n, m) = list(map(int, input().split()))
owes = [0 for i in range(n + 1)]
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    owes[a] += c
    owes[b] -= c
sol = 0
for owe in owes:
    if owe > 0:
        sol += owe
print(sol)
