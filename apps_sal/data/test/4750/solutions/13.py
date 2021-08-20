for _ in range(int(input())):
    (l1, r1, l2, r2) = list(map(int, input().split()))
    print(l1, l2 if l1 != l2 else l2 + 1)
