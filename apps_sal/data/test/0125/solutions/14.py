
S = []
for i in range(0, 4):
    S.append([bool(int(x)) for x in input().split()])


def check():
    for i in range(0, 4):
        for x in range(0, 3):
            if S[i][x] and (S[(i + abs(x - 3)) % 4][3] or S[i][3]):
                print("YES")
                return

    print("NO")


check()
