r, g, b = input().split()

ans = int(r) * 100 + int(g) * 10 + int(b)

if ans % 4 == 0:
    print("YES")
elif ans % 4 != 0:
    print("NO")
