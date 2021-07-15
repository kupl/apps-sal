x, k = map(int, input().split())
rounds = [False for i in range(x + 1)]
for i in range(k):
    line = list(map(int, input().split()))
    if line[0] == 1:
        rounds[line[1]] = True
        rounds[line[2]] = True
    else:
        rounds[line[1]] = True
maximum = rounds[1:x].count(False)
minimum = 0
i = x - 1
while i > 0:
    if i > 1 and rounds[i] == False and rounds[i - 1] == False:
        i -= 2
        minimum += 1
    elif rounds[i] == False:
        i -= 1
        minimum += 1
    else:
        i -= 1
print(minimum, maximum)
