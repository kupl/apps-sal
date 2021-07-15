n, k = map(int, input().split())
s = input()
i = s.find("G")
ans = False
while i < n:
    if s[i] == "#":
        break
    if s[i] == "T":
        ans = True
        break
    i += k
i = s.find("G")
while i > -1:
    if s[i] == "#":
        break
    if s[i] == "T":
        ans = True
        break
    i -= k
if ans:
    print("YES")
else:
    print("NO")
