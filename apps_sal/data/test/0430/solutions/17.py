n = int(input())
ds = len([s for s in input().split() if s == "200"])
cs = n - ds

if (cs % 2) == 1:
    print("NO")
elif cs > 1:
    print("YES")
elif ds % 2 == 1:
    print("NO")
else:
    print("YES")
