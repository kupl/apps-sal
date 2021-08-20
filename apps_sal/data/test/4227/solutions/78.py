import itertools
(n, m) = map(int, input().split())
li = []
for _ in range(m):
    (a, b) = map(int, input().split())
    li.append([a, b])
count = 0
for comb in itertools.permutations(range(n), n):
    if comb[0] != 0:
        continue
    judge = True
    for i in range(n - 1):
        if judge == False:
            break
        a = comb[i] + 1
        b = comb[i + 1] + 1
        if [a, b] in li or [b, a] in li:
            continue
        else:
            judge = False
            break
    if judge == True:
        count += 1
print(count)
