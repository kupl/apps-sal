for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    if n == 2 and m == 2:
        print("YES")
        continue
    if n == 1 or m == 1:
        print("YES")
        continue
    print("NO")
