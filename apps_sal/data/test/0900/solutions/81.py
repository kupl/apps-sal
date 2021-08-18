M = 10**9 + 7
text = input()
lst = list(text)
lst.reverse()
digit = len(lst)

six = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
for i in range(digit):
    if(lst[i] == "?"):
        six[i % 6][1] = six[i % 6][1] + 1
    else:
        six[i % 6][0] = (six[i % 6][0] + int(lst[i])) % 13


rem = -(six[0][0] - 3 * six[1][0] - 4 * six[2][0] -
        1 * six[3][0] + 3 * six[4][0] + 4 * six[5][0] - 5) % 13


def mat1(ls):
    val_ls = [0] * 13
    for i in range(13):
        val_ls[i] = (ls[i] + ls[(i - 1) % 13] + ls[(i - 2) % 13] +
                     ls[(i - 3) % 13] + ls[(i - 4) % 13] + ls[(i - 5) % 13] +
                     ls[(i - 6) % 13] + ls[(i - 7) % 13] + ls[(i - 8) % 13] +
                     ls[(i - 9) % 13]) % M
    return val_ls


def mat10(ls):
    val_ls = [0] * 13
    for i in range(13):
        val_ls[i] = (ls[i] + ls[(i + 3) % 13] + ls[(i + 6) % 13] +
                     ls[(i + 9) % 13] + ls[(i + 12) % 13] + ls[(i + 15) % 13] +
                     ls[(i + 18) % 13] + ls[(i + 21) % 13] + ls[(i + 24) % 13] +
                     ls[(i + 27) % 13]) % M
    return val_ls


def mat100(ls):
    val_ls = [0] * 13
    for i in range(13):
        val_ls[i] = (ls[i] + ls[(i + 4) % 13] + ls[(i + 8) % 13] +
                     ls[(i + 12) % 13] + ls[(i + 16) % 13] + ls[(i + 20) % 13] +
                     ls[(i + 24) % 13] + ls[(i + 28) % 13] + ls[(i + 32) % 13] +
                     ls[(i + 36) % 13]) % M
    return val_ls


def mat1000(ls):
    val_ls = [0] * 13
    for i in range(13):
        val_ls[i] = (ls[i] + ls[(i + 1) % 13] + ls[(i + 2) % 13] +
                     ls[(i + 3) % 13] + ls[(i + 4) % 13] + ls[(i + 5) % 13] +
                     ls[(i + 6) % 13] + ls[(i + 7) % 13] + ls[(i + 8) % 13] +
                     ls[(i + 9) % 13]) % M
    return val_ls


def mat10000(ls):
    val_ls = [0] * 13
    for i in range(13):
        val_ls[i] = (ls[i] + ls[(i - 3) % 13] + ls[(i - 6) % 13] +
                     ls[(i - 9) % 13] + ls[(i - 12) % 13] + ls[(i - 15) % 13] +
                     ls[(i - 18) % 13] + ls[(i - 21) % 13] + ls[(i - 24) % 13] +
                     ls[(i - 27) % 13]) % M
    return val_ls


def mat100000(ls):
    val_ls = [0] * 13
    for i in range(13):
        val_ls[i] = (ls[i] + ls[(i - 4) % 13] + ls[(i - 8) % 13] +
                     ls[(i - 12) % 13] + ls[(i - 16) % 13] + ls[(i - 20) % 13] +
                     ls[(i - 24) % 13] + ls[(i - 28) % 13] + ls[(i - 32) % 13] +
                     ls[(i - 36) % 13]) % M
    return val_ls


modulos = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for j in range(six[0][1]):
    modulos = mat1(modulos)
for j in range(six[1][1]):
    modulos = mat10(modulos)
for j in range(six[2][1]):
    modulos = mat100(modulos)
for j in range(six[3][1]):
    modulos = mat1000(modulos)
for j in range(six[4][1]):
    modulos = mat10000(modulos)
for j in range(six[5][1]):
    modulos = mat100000(modulos)
print((modulos[rem]))
