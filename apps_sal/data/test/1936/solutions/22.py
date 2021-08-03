for tc in range(int(input())):
    L, R = map(int, input().split())
    if L * 2 <= R:
        print(L, L * 2)
    else:
        print("-1 -1")
