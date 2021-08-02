import heapq
X, Y, A, B, C = map(int, input().split())
Plist = list(map(int, input().split()))
Qlist = list(map(int, input().split()))
Rlist = list(map(int, input().split()))
Plist.sort(reverse=True)
Qlist.sort(reverse=True)
Rlist.sort(reverse=True)
i, j, k = 0, 0, 0
pmax = Plist[i]
qmax = Qlist[i]
rmax = Rlist[i]
Ans = 0
for _ in range(2 * 10**5):
    Ans += max(pmax, qmax, rmax)
    if pmax == max(pmax, qmax, rmax):
        i += 1
        if i != X:
            pmax = Plist[i]
        else:
            pmax = -1
    elif qmax == max(pmax, qmax, rmax):
        j += 1
        if j != Y:
            qmax = Qlist[j]
        else:
            qmax = -1
    else:
        k += 1
        try:
            rmax = Rlist[k]
        except:
            rmax = -1
    if i + j + k == X + Y:
        break
print(Ans)
