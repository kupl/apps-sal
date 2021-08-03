for _ in range(int(input())):
    for a, b, c in zip(input(), input(), input()):
        if c not in (a, b):
            print("NO")
            break
    else:
        print("YES")
