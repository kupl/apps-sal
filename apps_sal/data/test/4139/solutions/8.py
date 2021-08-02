N = int(input())


def DFS(s):
    if int(s) > N:
        return 0
    if "7" in s and "5" in s and "3" in s:
        ret = 1
    else:
        ret = 0
    for c in "753":
        ret += DFS(s + c)
    return ret


print(DFS("0"))
