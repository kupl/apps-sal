h, n = map(int, input().split())
A = list(map(int, input().split()))
flag = False

for a in A:
    h -= a
    if h <= 0:
        flag = True
        break

print("Yes" if flag else "No")
