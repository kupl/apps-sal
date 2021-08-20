n = int(input())
room = set()
cap = 0
for i in range(n):
    (typ, r) = input().split()
    if typ == '+':
        room.add(r)
    elif r in room:
        room.remove(r)
    else:
        cap += 1
    cap = max(cap, len(room))
print(cap)
