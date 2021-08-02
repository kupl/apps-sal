a, b = list(map(int, input().split()))
s = sorted(input())

last = '$'
cost = 0
used = 0

for c in s:
    if ord(c) - ord(last) > 1:
        cost += ord(c) - ord('a') + 1
        used += 1
        last = c
    if used == b:
        break

if used == b:
    print(cost)
else:
    print(-1)
