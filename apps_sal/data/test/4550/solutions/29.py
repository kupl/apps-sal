l = list(map(int, input().split()))
l1 = sorted(l, reverse=True)
s = sum(l1)
if l1[0] == s / 2:
    print("Yes")
else:
    print("No")
