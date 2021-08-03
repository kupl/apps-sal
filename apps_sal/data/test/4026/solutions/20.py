t = int(input())
for test in range(1, t + 1):
    n, m = [int(i) for i in input().split()]
    flag = False
    for i in range(n):
        a, b = [int(j) for j in input().split()]
        c, d = [int(j) for j in input().split()]
        if b == c:
            flag = True
    if flag and m % 2 == 0:
        print("YES")
    else:
        print("NO")
