def check(hint, Card):
    for i in Card:
        for j in Card:
            if i == j:
                continue
            elif i[0] == j[0]:
                if i[1] not in hint and j[1] not in hint:
                    return False
            elif i[1] == j[1]:
                if i[0] not in hint and j[0] not in hint:
                    return False
            else:
                if i[0] not in hint and i[1] not in hint and j[0] not in hint and j[1] not in hint:
                    return False
    return True


HH = "RGBYW12345"
n = int(input())
Card = list(input().split(' '))
ans = 20
for i in range(1024):
    hint = ""
    cnt = 0
    for j in range(10):
        if (2**j) & i > 0:
            hint += HH[j]
            cnt += 1
    if check(hint, Card):
        ans = min(ans, cnt)
print(ans)
