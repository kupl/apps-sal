st = input()
otv = ""
if len(st) % 2 == 0:
    i = 1
    while i <= len(st) // 2:
        otv = st[-i] + otv
        otv = st[i - 1] + otv
        i += 1
    print(otv)
else:
    i = 0
    while i < len(st) // 2:
        otv = st[i] + otv
        otv = st[-i - 1] + otv
        i += 1
    otv = st[len(st) // 2] + otv
    print(otv)
