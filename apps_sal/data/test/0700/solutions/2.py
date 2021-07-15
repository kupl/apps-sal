n=int(input())
ns=[]
for i in range(n):
    s=input()
    ns.append(s)
ns2=[]
for i in range(n):
    s=input()
    ns2.append(s)


def rotate(i,j):
    return j,n-1-i
def flip(i,j):
    return j,i

def main():
    same=True
    for i in range(n): # 0
        for j in range(n):
            if ns[i][j]!=ns2[i][j]:
                same=False
                break
        if same==False:
            break
    if same:
        return True

    same=True
    for i in range(n):  # 1
        for j in range(n):
            a, b = rotate(i, j)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same=True
    for i in range(n):  # 2
        for j in range(n):
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same=True
    for i in range(n):
        for j in range(n):  # 3
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = rotate(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same=True
    for i in range(n): # 0
        for j in range(n):
            a,b=flip(i,j)
            if ns[a][b]!=ns2[i][j]:
                same=False
                break
        if same==False:
            break
    if same:
        return True

    same=True
    for i in range(n):  # 1
        for j in range(n):
            a, b = rotate(i, j)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same=True
    for i in range(n):  # 2
        for j in range(n):
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True

    same=True
    for i in range(n):
        for j in range(n):  # 3
            a, b = rotate(i, j)
            a, b = rotate(a, b)
            a, b = rotate(a, b)
            a, b = flip(a, b)
            if ns[i][j] != ns2[a][b]:
                same = False
                break
        if same == False:
            break
    if same:
        return True
    else:
        return False

if main():
    print('Yes')
else:
    print('No')




