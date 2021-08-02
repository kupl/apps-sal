n = int(input())
seats = []
ans = ""
for i in range(n):
    s = input()
    ss = s.split("|")
    s1 = ss[0]
    if ans == "" and ss[0] == "OO":
        ans = "YES"
        s1 = "++"
    s2 = ss[1]
    if ans == "" and ss[1] == "OO":
        ans = "YES"
        s2 = "++"
    seats.append(s1 + "|" + s2)

if ans != "":
    print(ans)
    print("\n".join(seats))
else:
    print("NO")
