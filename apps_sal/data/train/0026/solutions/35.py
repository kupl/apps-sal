t = int(input())
for i in range(t):
    n, m = list(map(int, input().split()))
    if min(n, m) == 1 or m == 2 and n == 2:
        print("YES")
    else:
        print("NO")
