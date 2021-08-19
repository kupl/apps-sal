def readln():
    return list(map(int, input().split()))


(n, k) = readln()
dirties = []
if k > 0:
    dirties = readln()
dirties = sorted(dirties)
prevprev = -1
prev = -1
ilegal = False
for val in dirties:
    if prevprev == -1:
        prevprev = val
        continue
    if prev == -1:
        prev = val
        continue
    if prevprev == prev - 1 and prev == val - 1:
        ilegal = True
    prevprev = prev
    prev = val
if ilegal or (k > 0 and (dirties[0] == 1 or dirties[-1] == n)):
    print('NO')
else:
    print('YES')
