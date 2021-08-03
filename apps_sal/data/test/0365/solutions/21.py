n, x = list(map(int, input().split()))
s = sum(list(map(int, input().split())))
if s + n - 1 == x:
    print("YES")
else:
    print("NO")
