tc = int(input())
for _ in range(tc):
    n = int(input())
    if n > 1:
        print("2" + "3" * (n - 1))
    else:
        print(-1)
