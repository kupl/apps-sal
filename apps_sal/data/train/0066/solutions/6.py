for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    l1.sort()
    l2.sort()
    print(*l1, sep=" ")
    print(*l2, sep=" ")
