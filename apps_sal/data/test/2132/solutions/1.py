# D. Driving Test

n = int(input())

ps = None
seen_sl = [float('inf')]
seen_ot = [True]

answer = 0
for i in range(n):
    line = list(map(int, input().split()))
    t = line[0]
    if t == 1:
        ps = line[1]
        while ps > seen_sl[-1]:
            answer += 1
            seen_sl.pop(-1)
    elif t == 2:
        while not seen_ot[-1]:
            answer += 1
            seen_ot.pop(-1)
    elif t == 3:
        seen_sl.append(line[1])
        while ps > seen_sl[-1]:
            answer += 1
            seen_sl.pop(-1)
    elif t == 4:
        seen_ot.append(True)
    elif t == 5:
        seen_sl.append(float('inf'))
    elif t == 6:
        seen_ot.append(False)

print(answer)
