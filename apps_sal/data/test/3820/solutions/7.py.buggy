n, m = list(map(int, input().strip().split()))
r = input()
s = input()
if "*" not in r:
    if r == s:
        print("YES")
    else:
        print("NO")
    return
r1, r2 = r.split("*")
if len(s) < (len(r1) + len(r2)):
    print("NO")
else:
    l1 = len(r1)
    l2 = len(r2)
    if s[0:l1] == r1 and s[len(s) - l2:] == r2:
        print("YES")
    else:
        print("NO")
