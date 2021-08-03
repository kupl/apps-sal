a = sorted(list(map(int, input().split())))
if sum(a[:2]) == a[2]:
    print("Yes")
else:
    print("No")
