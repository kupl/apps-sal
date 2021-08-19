nc = input().split()
nc = [int(nc[i]) for i in range(2)]
p = input().split()
p = [int(p[i]) for i in range(nc[0])]
t = input().split()
t = [int(t[i]) for i in range(nc[0])]
limak = 0
radewoosh = 0
time = 0
for prob in range(nc[0]):
    time += t[prob]
    limak += max(0, p[prob] - nc[1] * time)
time = 0
for prob in range(nc[0] - 1, -1, -1):
    time += t[prob]
    radewoosh += max(0, p[prob] - nc[1] * time)
if limak > radewoosh:
    print('Limak')
elif limak < radewoosh:
    print('Radewoosh')
else:
    print('Tie')
