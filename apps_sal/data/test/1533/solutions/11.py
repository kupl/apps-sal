n = int(input())
s = []
for i in range(n):
    x = input()
    if x not in s:
        s.append(x)
        print("NO")
    else:
        print("YES")
