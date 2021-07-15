n = int(input())

room = set()
maximum = 0
for _ in range(n):
    t, r = input().split()
    r = int(r)
    if t == '+':
        room.add(r)
        maximum = max(maximum, len(room))
    else:
        if r in room:
            room.remove(r)
        else:
            maximum += 1

print(maximum)
