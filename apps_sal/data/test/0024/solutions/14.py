rs = []
for i in range(10):
    length = input()
    rs.append(length)
temp1 = 1
flag1 = 1

def check(i, j, direct,temp,flag):
    if direct == 1:
        if j == 0:
            return 0
        j -= 1
    elif direct == 2:
        if j == 9:
            return 0
        j += 1
    elif direct == 3:
        if i == 0:
            return 0
        i -= 1
    elif direct == 4:
        if i == 9:
            return 0
        i += 1
    elif direct == 5:
        if i == 0 or j == 0:
            return 0
        j -= 1
        i -= 1
    elif direct == 6:
        if i == 9 or j == 0:
            return 0
        j -= 1
        i += 1
    elif direct == 7:
        if i == 0 or j == 9:
            return 0
        j += 1
        i -= 1
    elif direct == 8:
        if i == 9 or j == 9:
            return 0
        j += 1
        i += 1
    if rs[i][j] == 'X':
        temp += 1
        if(temp > 4):
            return 1
        return check(i,j,direct,temp,flag)
    elif rs[i][j] == '.' and flag == 1:
        temp += 1
        flag = 0
        if(temp > 4):
            return 1
        return check(i,j,direct,temp,flag)
    else:
        return 0  

def result():
    for i in range(10):
        for j in range(10):
            if rs[i][j] == 'X':
                for k in range(1,9):
                    if check(i,j,k,temp1,flag1) == 1:
                        return 1
    return 0
if result() == 0:
    print("NO")
else:
    print("YES")

