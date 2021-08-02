n = int(input())
s = list(map(int, input().split()))
r = [n]
while r[-1] != 1:
    r.append(s[r[-1] - 2])
print(*reversed(r))
