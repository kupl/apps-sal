t = int(input())
A = [input() for i in range(t)]


for a in A:
    ANS = sorted(list(a))

    if ANS[0] == ANS[-1]:
        print(-1)
        continue

    else:
        for a in ANS:
            print(a, end="")

        print()
