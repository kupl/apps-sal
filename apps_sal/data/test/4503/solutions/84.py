attack = []
(h, n) = map(int, input().split())
a = input().split()
for move in a:
    move = int(move)
    attack.append(move)
result = h - sum(attack)
if result <= 0:
    print('Yes')
else:
    print('No')
