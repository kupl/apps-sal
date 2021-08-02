n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
a_max = max(a)
flg = False
if a.count(a_max) > 1:
    flg = True
a_s = sorted(a, reverse=True)
for ai in a:
    if ai != a_max:
        print(a_max)
    elif flg:
        print(a_max)
    else:
        print(a_s[1])
