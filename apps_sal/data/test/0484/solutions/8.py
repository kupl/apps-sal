n, a, b = map(int, input().split())
s = []
for i in range(n):
    x, y = map(int, input().split())
    s.append((x, y, x*y))
t = 0
for i in range(n):
    for j in range(i):
        if (s[i][0]+s[j][0]<=a and s[i][1]<=b and s[j][1] <=b) or (s[i][1]+s[j][0]<=a and s[i][0]<=b and s[j][1] <=b) or (s[i][0]+s[j][1]<=a and s[i][1]<=b and s[j][0] <=b) or (s[i][1]+s[j][1]<=a and s[i][0]<=b and s[j][0] <=b):
            t = max(t, s[i][2]+s[j][2])
        a, b = b, a
        if (s[i][0]+s[j][0]<=a and s[i][1]<=b and s[j][1] <=b) or (s[i][1]+s[j][0]<=a and s[i][0]<=b and s[j][1] <=b) or (s[i][0]+s[j][1]<=a and s[i][1]<=b and s[j][0] <=b) or (s[i][1]+s[j][1]<=a and s[i][0]<=b and s[j][0] <=b):
            t = max(t, s[i][2]+s[j][2])
        a,b = b, a
print(t)
