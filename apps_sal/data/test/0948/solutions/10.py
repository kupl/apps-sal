n, m = [int(i) for i in input().split()]
s = []
o = 0
for t in range(n):
    s.append(input())
for i in range(n-1):
    for j in range(m-1):
        a = s[i][j]+s[i][j+1]+s[i+1][j]+s[i+1][j+1]
        if "f" in a and "c" in a and "e" in a and "a" in a:
            o+=1
print(o)

