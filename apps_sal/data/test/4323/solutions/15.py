import sys

n, m = map(int, sys.stdin.readline().split())
song = [None]*n
somme = 0
for loop in range(n):
    d, f = map(int, sys.stdin.readline().split())
    somme += d
    song[loop] = d-f
song.sort(reverse=True)
total = 0
while total < n and somme > m:
    somme-= song[total]
    total += 1
if somme > m:
    print(-1)
else:
    print(total)
