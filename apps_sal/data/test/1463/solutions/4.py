n = int(input())
s = []
for k in range(n):
    s.append([int(i) for i in input().split()])
t = 0
for i in range(n):
    for j in range(n):
        l = 0
        if s[i][j] !=1:
            for x in range(n):
                for y in range(n):
                    if s[i][x]+ s[y][j] == s[i][j]:
                        l = 1
            if not l:
                t = 1
if t:
    print("No")
else:
    print("Yes")

