for _ in range(int(input())):
    (x, y) = map(int, input().split())
    (a, b) = map(int, input().split())
    common = min(x, y)
    if 2 * common * a <= common * b:
        print(x * a + y * a)
    else:
        print(common * b + (max(x, y) - common) * a)
