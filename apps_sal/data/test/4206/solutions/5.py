s = input()
ost = []
for i in map(int, s):
    ost += [i % 3]
now = 0
last = -1
answer = 0
for i in ost:
    if i == 0:
        now = []
        answer += 1
    else:
        if now == 2:
            now = 0
            answer += 1
        elif now == 1:
            if last != i:
                answer += 1
                now = 0
            else:
                now = 2
        else:
            now = 1
            last = i
print(answer)
