(n, pos, l, r) = list(map(int, input().split()))
if l == 1 and r == n:
    print(0)
elif l == 1 and r != n:
    print(abs(pos - r) + 1)
elif l != 1 and r == n:
    print(abs(pos - l) + 1)
elif l <= pos <= r:
    print(r - l + 2 + min(abs(pos - l), abs(pos - r)))
elif pos < l:
    print(r - l + 2 + abs(pos - l))
else:
    print(r - l + 2 + abs(pos - r))
