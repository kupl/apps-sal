from sys import stdin

(n, m) = list(map(int, input().split()));
nb = list(map(int, input().split()))

nb.sort();

minDiff = nb[m-1]
for i in range(n-1, m):
    minDiff = min(minDiff, nb[i] - nb[i-n+1])

print(minDiff)

