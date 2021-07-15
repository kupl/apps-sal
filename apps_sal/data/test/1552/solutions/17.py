n = int(input())
ti2 = list(map(str,input().split()))
ti = "".join(ti2)
mis = 0
k = 0
ki = [[0] * 3 for i in range(n//3)]

while mis == 0:
    p = ti.find("1")
    m = ti.find("2")
    f = ti.find("3")
    if p!=-1 and m!=-1 and f!=-1:
        ti2[p] = "4"
        ti2[m] = "4"
        ti2[f] = "4"
        ti = "".join(ti2)
        ki[k][0]=p+1
        ki[k][1]=m+1
        ki[k][2]=f+1
        k+=1
    else:
        mis=1
print(k)
for y in range(k):
    for x in range(3):
        print(ki[y][x],end=" ")
    print()

