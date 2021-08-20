n = int(input())
strength = list(map(int, input().split()))
pieces = input()
bob = 0
for (pos, p) in enumerate(pieces):
    if p == 'B':
        bob += strength[pos]
best_flip = 0
cur_flip = 0
for (st, p) in zip(strength, pieces):
    if p == 'A':
        cur_flip += st
    else:
        cur_flip -= st
    best_flip = max(best_flip, cur_flip)
cur_flip = 0
for (st, p) in zip(reversed(strength), reversed(pieces)):
    if p == 'A':
        cur_flip += st
    else:
        cur_flip -= st
    best_flip = max(best_flip, cur_flip)
print(bob + best_flip)
