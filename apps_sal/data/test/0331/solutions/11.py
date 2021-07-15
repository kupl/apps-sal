from sys import stdin, stdout

n, m, k = map(int, stdin.readline().split())
challengers = list(map(int, stdin.readline().split()))
m -= 1

i = 1
ans = 10
while True:
    if m + i < n and challengers[m + i] and challengers[m + i] <= k:
        break
    
    if m - i >= 0 and challengers[m - i] and challengers[m - i] <= k:
        break
    
    ans += 10
    i += 1


stdout.write(str(ans))
