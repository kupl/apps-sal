n = int(input())
weights = list(map(int, input().split()))

if weights.count(200) % 2 == 0:
    if weights.count(100) % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    if weights.count(100) % 2 == 0 and weights.count(100) >= 2:
        print("YES")
    else:
        print("NO")
