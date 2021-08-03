n = int(input())
for i in range(n):
    input()
    s = input()
    b = int(s[0])
    c = int(s[1:])
    if b < c:
        print("YES")
        print(2)
        print(b, c)
    else:
        print("NO")
