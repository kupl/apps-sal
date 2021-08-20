t = int(input())
NK = [list(map(int, input().split())) for i in range(t)]
for i in range(t):
    (n, k) = NK[i]
    for j in range(n):
        print(chr(97 + j % k), end='')
    print()
