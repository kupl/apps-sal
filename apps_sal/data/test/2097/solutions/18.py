for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = sum(l)
    z = l.count(0)
    count = z
    s += z
    if s == 0:
        count += 1
    print(count)
