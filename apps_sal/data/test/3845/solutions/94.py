A,B = list(map(int,input().split()))
if A==1:
    C = [["." for _ in range(100)] for _ in range(100)]
    cnt = 0
    flag=0
    for i in range(0,100,2):
        for j in range(0,100,2):
            C[i][j] = "#"
            cnt += 1
            if cnt==B:
                flag = 1
                break
        if flag==1:
            break
elif B==1:
    C = [["#" for _ in range(100)] for _ in range(100)]
    cnt = 0
    flag = 0
    for i in range(0,100,2):
        for j in range(0,100,2):
            C[i][j] = "."
            cnt += 1
            if cnt==A:
                flag = 1
                break
        if flag==1:
            break
else:
    C = [["." for _ in range(100)] for _ in range(100)]
    for i in range(50,100):
        for j in range(100):
            C[i][j] = "#"
    for i in range(1,49):
        for j in range(1,99):
            C[i][j] = "#"
    cnt = 0
    flag = 0
    for i in range(2,47,2):
        for j in range(2,97,2):
            if cnt==A-2:
                flag = 1
                break
            C[i][j] = "."
            cnt += 1
        if flag==1:break
    for i in range(51,99):
        for j in range(1,99):
            C[i][j] = "."
    cnt = 0
    flag = 0
    for i in range(52,97,2):
        for j in range(2,97,2):
            if cnt==B-2:
                flag = 1
                break
            C[i][j] = "#"
            cnt += 1
        if flag==1:break
print((100,100))
for i in range(100):
    print(("".join(C[i])))

