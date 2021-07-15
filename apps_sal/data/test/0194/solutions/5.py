n,a,b = list(map(int,input().split()))
line = input().split()
t = []
c = 0
rej = 0
for i in range(n):
    t.append(int(line[i]))
for i in range(n):
    if a > 0 and t[i] == 1:
        a -= 1
    elif t[i] == 1 and b > 0:
        b -= 1
        c += 1
    elif t[i] == 1 and c > 0:
        c -= 1
    elif t[i] == 2 and b > 0:
        b -= 1
    else:
        rej += t[i]
print(rej)

