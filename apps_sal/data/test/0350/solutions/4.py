n, a, s, v = int(input()), sorted(map(int, input().split()), reverse=True), set(), 0
for ai in a:
    while ai and ai in s:
        ai -= 1
    s.add(ai)
    v += ai
print(v)
