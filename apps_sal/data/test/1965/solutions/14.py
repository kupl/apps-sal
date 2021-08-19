for _ in range(int(input())):
    (n, x) = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if set(arr) == {x}:
        print(0)
        continue
    s = sum(arr)
    if s // n * n == s and s // n == x or x in arr:
        print(1)
    else:
        print(2)
