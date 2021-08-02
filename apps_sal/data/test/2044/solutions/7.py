n, m = map(int, input().split())
a = list(map(int, input().split()))
left = m
for x in a:
    turn = 0
    if x < left:
        left -= x
    else:
        x -= left
        turn = 1 + x // m
        left = m - x % m
    print(turn, end=' ')
print()
