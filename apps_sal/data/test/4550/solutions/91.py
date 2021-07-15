l = sorted(list(map(int, input().split())))
print("Yes" if l[2] == sum(l[:2]) else "No")
