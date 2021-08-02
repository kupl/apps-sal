n = int(input())

statements = []

for i in range(n):
    a = int(input())
    astates = [list(map(int, input().split())) for _ in range(a)]

    statements.append(astates)

cnt = 0
for i in range(2**n):
    state = format(i, "0" + str(n) + "b")

    pos = True
    for j in range(n):
        if state[j] == "1":
            for x, y in statements[j]:
                if not (state[x - 1] == str(y)):
                    pos = False
                    break

        if not pos:
            break

    if pos:
        cnt = max(cnt, state.count("1"))

print(cnt)
