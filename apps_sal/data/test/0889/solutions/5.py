def getField():
    field = []
    for i in range(0, 4):
        field.append(input())
    return field


def canPass(field):
    for i in range(0, 3):
        for j in range(0, 3):
            if field[i][j] == field[i + 1][j] == field[i + 1][j + 1]:
                return True
    return False


def canPassTotal(field):
    res = False
    for i in range(0, 4):
        res = res or canPass(field)
        field = rot(field)
    return res


def rot(mat):
    mat = [mat[i] for i in range(len(mat) - 1, -1, -1)]
    t = [[x[i] for x in mat] for i in range(0, len(mat[0]))];
    return t


ans = {'True': 'YES', 'False': 'NO'}
print(ans[str(canPassTotal(getField()))])
