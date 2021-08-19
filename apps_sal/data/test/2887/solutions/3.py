# cook your dish here
t = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))
if t == 0 or t == 1:
    print(0)
else:
    for i in range(t):
        c = 0
        p = s[0:i + 1]
        for j in range(len(p)):
            if p[j] >= e[i]:
                c += e[i]
                s[j] -= e[i]
            else:
                c += p[j]
                s[j] = 0
        print(c, end=" ")
