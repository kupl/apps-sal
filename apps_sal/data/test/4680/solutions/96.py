arr = list(map(int, input().split()))

if arr.count(5) == 2 and arr.count(7) == 1:
    print("YES")
else:
    print("NO")
