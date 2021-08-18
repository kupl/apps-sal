# na-
import itertools
H, W, K = map(int, input().split())
S = [list(map(int, list(input()))) for _ in range(H)]


def check(k):
    if k <= K:
        return(True)
    else:
        return(False)


noans = 0


def make_lst(i):
    nonlocal noans, lst, havelst
    temp = S[0][i]
    for h in range(H - 1):
        if y[h]:
            lst.append(temp)
            temp = S[h + 1][i]
        else:
            temp += S[h + 1][i]
    lst.append(temp)
    if check(max(lst)):
        havelst = 1
    else:
        noans = 1


def nocut(i):
    nonlocal cutnum, lst, havelst
    prelst = []
    temp = S[0][i]
    j = 0
    for h in range(H - 1):
        if y[h]:
            lst[j] += temp
            prelst.append(temp)
            j += 1
            temp = S[h + 1][i]
        else:
            temp += S[h + 1][i]
    prelst.append(temp)
    lst[-1] += temp
    if check(max(lst)):
        return(True)
    else:
        cutnum += 1
        lst = prelst


ans = float("inf")
cutlst = []
for y in itertools.product((0, 1), repeat=H - 1):
    havelst = 0
    lst = []
    cutnum = sum(y)
    for x in range(W):
        if noans:
            break
        if havelst:
            nocut(x)
        else:
            make_lst(x)
    if noans == 1:
        noans = 0
        continue
    ans = min(cutnum, ans)
print(ans)
