a = list(map(int, input().split()))
s = sum(a)
a.sort(reverse=True)
if s % 2 == 1:
    print("No")
else:
    if s // 2 == a[0] or s // 2 == a[0] + a[-1]:
        print("Yes")
    else:
        print("No")
