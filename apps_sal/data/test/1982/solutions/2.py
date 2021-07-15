def solve():
    n, k = list(map(int, input().split()))
    s = k ** 2
    if n < s:
        print("NO")
    else:
        if (k % 2) ^ (n % 2) == 0:
            print("YES")
        else:
            print("NO")


for i in range(int(input())):
    solve()

