for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    typ = list(map(int, input().split()))

    if len(set(typ)) == 2:
        print("Yes")
        continue

    prev = -1
    flag = True
    for e in arr:
        if e < prev:
            flag = False
            break
        prev = e

    if flag:
        print("Yes")
    else:
        print("No")
