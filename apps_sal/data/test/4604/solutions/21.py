n = int(input())
a = sorted(list(map(int, input().split())))
if len(a) % 2 == 1:
    tmp = [0]
    for i in range((len(a) - 1) // 2):
        tmp.append((i + 1) * 2)
        tmp.append((i + 1) * 2)
    if a == tmp:
        ans = 2 ** ((len(a) - 1) // 2) % (10 ** 9 + 7)
    else:
        ans = 0
else:
    tmp = []
    for i in range(len(a) // 2):
        tmp.append(2 * i + 1)
        tmp.append(2 * i + 1)
    if a == tmp:
        ans = 2 ** (len(a) // 2) % (10 ** 9 + 7)
    else:
        ans = 0
print(ans)
