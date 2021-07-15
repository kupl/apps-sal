ts = int(input())

for ti in range(ts):
    n = int(input())
    s = input()
    pos = -1
    for i in range(n):
        if s[i] == "8":
            pos = i
            break
    if pos != -1 and n - pos >= 11:
        print("YES")
    else:
        print("NO")

