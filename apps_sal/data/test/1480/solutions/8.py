n, _ = [int(i) for i in input().strip().split(' ')]
ak = [int(i) for i in input().strip().split(' ')]


people = list(range(1, n + 1))
current = 0

leaved = []

for k in ak:
    pos = ((current + k) % len(people))
    leave = people.pop(pos)

    leaved.append(leave)

    if pos >= len(people):
        current = 0
    else:
        current = pos

print(" ".join(map(str, leaved)))

