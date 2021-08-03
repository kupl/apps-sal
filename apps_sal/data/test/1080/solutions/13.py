n = int(input())
a = list(map(int, input().split()))
if sum(a) % 2:
    print("NO")
else:
    a.sort()
    if sum(a[:n - 1]) - a[-1] < 0:
        print("NO")
    else:
        print("YES")
