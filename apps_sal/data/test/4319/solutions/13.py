n = int(input())
answer = []
kol = 0
for i in input().split():
    if i == '1':
        answer.append(kol)
        kol = 1
    else:
        kol += 1
answer.append(kol)
answer.pop(0)
print(len(answer))
print(*answer)
