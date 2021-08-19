n = int(input())
a = list(map(int, input().split()))
pos1 = a.index(1) + 1
posn = a.index(n) + 1
res = abs(pos1 - posn)
res = max(res, abs(1 - pos1))
res = max(res, abs(n - pos1))
res = max(res, abs(1 - posn))
res = max(res, abs(n - posn))
print(res)
