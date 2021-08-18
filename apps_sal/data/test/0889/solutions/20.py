def main(l):
    for i in range(3):
        for j in range(3):
            x = l[i][j] + l[i][j + 1] + l[i + 1][j] + l[i + 1][j + 1]
            if(5 > str.count(x, '.') > 2):
                return True
            if(5 > str.count(x, '
                return True
    return False


l=[]
for m in range(4):
    l += [input()]
if(main(l) == True):
    print("YES")
else:
    print("NO")
