tests = int(input())
for tests in range(tests):
    n = int(input())
    if n <= 30:
        print("NO")
    else:
        print("YES")
        if n - 30 in [14, 6, 10]:
            print(15, 6, 10, n - 31)
        else:
            print(14, 6, 10, n - 30)
