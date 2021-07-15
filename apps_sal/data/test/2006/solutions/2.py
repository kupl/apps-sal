n, m = map(int, input().split())
dist_w = 2001
dist_s = -1
flag = False
ans = set()
for i in range(n): 
    s = input()
    gnome = s.find("G")
    sweet = s.find("S")
    if gnome > sweet:
        flag = True
        break
    ans.add(sweet - gnome)
if flag:
    print(-1)
else:
    print(len(ans))
