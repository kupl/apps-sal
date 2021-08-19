for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(0 if a == [x] * n else 1 if x in a or sum((x - y for y in a[1:])) == a[0] - x else 2)
