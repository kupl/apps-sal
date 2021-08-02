n, m, x, y = map(int, input().split())
lx = list(map(int, input().split()))
ly = list(map(int, input().split()))
z = max(lx) + 1 if max(lx) >= x else x + 1

if min(ly) < z or y < z:
    print("War")

else:
    print("No War")
