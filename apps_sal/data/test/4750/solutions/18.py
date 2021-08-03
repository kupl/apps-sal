for _ in range(int(input())):
    l1, r1, l2, r2 = map(int, input().split())
    for i in range(l2, r2 + 1):
        if i != l1:
            print(l1, i)
            break
