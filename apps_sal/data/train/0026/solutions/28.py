q = int(input())
for i in range(q):
    n, m = list(map(int, input().split()))
    if (n == 1 or m == 1):
        print("YES")
    elif (n == m == 2):
        print("YES")
    else:
        print("NO")

