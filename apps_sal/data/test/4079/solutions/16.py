N = int(input())


def diverse(t):
    t = sorted(t)
    for i in range(len(t)):
        if ord(t[i]) - ord(t[0]) != i:
            return 0
    return 1


for _ in range(N):
    if diverse(input()):
        print("Yes")
    else:
        print("No")
