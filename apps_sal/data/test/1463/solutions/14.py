# def proverka(b, k, m, p):
#  for i in range()

n = int(input())
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
flag = "Yes"
for i in range(n):
    for j in range(n):
        if(a[i][j] != 1):
            f = False
            for k in range(n):
                if(f):
                    break
                for z in range(n):
                    if(a[k][j] + a[i][z] == a[i][j]):
                        f = True
                    if(f):
                        break
            if(not(f)):
                flag = "No"

print(flag)
