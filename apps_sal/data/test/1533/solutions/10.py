a = set()
for i in range(int(input())):
    s = input()
    if s in a:
        print("YES")
    else:
        print("NO")
        a.add(s)
