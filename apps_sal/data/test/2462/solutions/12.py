# 6, 10, 15, 14

t = int(input())

for _ in range(t):
    n = int(input())

    if n <= 30:
        print("NO")
    else:
        print("YES")
        if n - 30 in [6, 10, 14]:
            print(6, 10, 15, n - 31)
        else:
            print(6, 10, 14, n - 30)
