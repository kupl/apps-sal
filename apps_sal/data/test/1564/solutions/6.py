
n = int(input())
s1 = input()
s2 = input()
if (s1.count('a') + s2.count('a')) % 2 == 1 or (s1.count('b') + s2.count('b')) % 2 == 1:
    print(-1)
    return

sort1 = []
sort2 = []
for i in range(n):
    if s1[i] != s2[i]:
        if s1[i] == 'a':
            sort1.append(i)
        else:
            sort2.append(i)
moves = []
while len(sort1) > 1:
    moves.append([sort1[-1], sort1[-2]])
    sort1.pop()
    sort1.pop()
while len(sort2) > 1:
    moves.append([sort2[-1], sort2[-2]])
    sort2.pop()
    sort2.pop()
if len(sort1) == 1:
    moves.append([sort1[0], sort1[0]])
    moves.append([sort1[0], sort2[0]])
print(len(moves))
for x in moves:
    print(x[0] + 1, x[1] + 1)

