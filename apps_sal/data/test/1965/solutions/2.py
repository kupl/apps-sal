def y():
    return map(int, input().split())


for _ in range(int(input())):
    (n, x) = y()
    a = [*y()]
    if all((i == x for i in a)):
        print(0)
        continue
    if x in a or sum(a) == x * n:
        print(1)
        continue
    print(2)
