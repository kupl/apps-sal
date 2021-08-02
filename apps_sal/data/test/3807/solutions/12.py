import math


def root(m):
    ret = m**(1.0 / 3.0)
    if(math.ceil(ret)**3 == m):
        ret = math.ceil(ret)
    else: ret = math.floor(ret)
    return ret


F = {}


def f(m):
    if(m < 0):
        return [-1e5 - 10, -1e15 - 1]
    if(m <= 7):
        return [m, m]
    rootm = root(m)
    ans1 = [0, 0]
    ans2 = [0, 0]
    ans1 = f(m - rootm**3)
    if(rootm != 1):
        ans2 = f(rootm**3 - 1 - (rootm - 1)**3);
        ans2[1] += (rootm - 1)**3;
        ans2[0] += 1;
    ans1[1] += rootm**3;
    ans1[0] += 1;
    if(ans1[0] > ans2[0]):
        return ans1
    elif(ans1[0] < ans2[0]):
        return ans2
    else:
        if(ans1[1] > ans2[1]):
            return ans1
        else:
            return ans2


m = int(input())
ans = f(m)
print(ans[0], ans[1])
