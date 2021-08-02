n = int(input().strip())
attempt1, attempt2, attempt3 = {}, {}, {}
for e in map(int, input().strip().split()):
    attempt1[e] = attempt1.get(e, 0) + 1

for e in map(int, input().strip().split()):
    attempt2[e] = attempt2.get(e, 0) + 1

for e in map(int, input().strip().split()):
    attempt3[e] = attempt3.get(e, 0) + 1

for e in attempt1:
    if e not in attempt2 or attempt2[e] < attempt1[e]:
        print(e)
        break

for e in attempt2:
    if e not in attempt3 or attempt3[e] < attempt2[e]:
        print(e)
        break
