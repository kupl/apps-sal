
nb = int(input())
boys = list(map(int, input().split(' ')))
ng = int(input())
girls = list(map(int, input().split(' ')))


matches = [[] for i in range(nb)]
for bi, boy in enumerate(boys):
    for i in range(ng):
        if girls[i] >= boy - 1 and girls[i] <= boy + 1:
            matches[bi].append(i)


def find(idx, taken, tried):
    for girl in matches[idx]:
        if not girl in tried:
            tried.add(girl)
            if not girl in taken or find(taken[girl], taken, tried):
                taken[girl] = idx
                return True
    return False


def getmax():
    result = 0
    taken = {}
    for bi, boy in enumerate(boys):
        tried = set()
        if find(bi, taken, tried):
            result += 1

    return result


print(getmax())
