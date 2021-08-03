n = int(input())
a = list(map(int, input().split()))
a.sort()
if a[-3] + a[-2] > a[-1]:
    print("YES")
    a[-1], a[-2] = a[-2], a[-1]
    print(*a)
else:
    print("NO")
