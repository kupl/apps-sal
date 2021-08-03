n, m = list(map(int, input().split()))
if(n + 1 == m or n - 1 == m or n == m):
    if(n == 0 and m == 0):
        print("NO")
    else:
        print("YES")
else:
    print("NO")
