N = int(input())

names = set()

T = 0
while T < N:
    T += 1
    name = input()
    if name in names:
        print("YES")
    else:
        print("NO")
        names.add(name)

