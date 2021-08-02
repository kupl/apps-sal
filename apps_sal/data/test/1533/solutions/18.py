n = int(input())
a = []
for i in range(n):
    name = input()
    if(a.count(name) != 0):
        print("YES")
    else:
        print("NO")
        a.append(name)
