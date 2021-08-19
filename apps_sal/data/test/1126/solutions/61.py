N, X, M = map(int, input().split())

ans = 0
sumlist = [X, ]
checklist = [-1] * (M + 1)
A = X
# checklist[A] = 0


def calcans(start, end, sumlist):
    cnt = end - start + 1
    loop = (N - start - 1) // cnt
    add = N - (cnt * loop) - start
    return (sumlist[end] - sumlist[start - 1]) * loop + sumlist[start - 1 + add]


for i in range(1, N):
    A = (A**2) % M
    # print(A)
    if checklist[A - 1] != -1:
        # print(f'start: {checklist[A]} end: {i-1}')
        ans = calcans(checklist[A - 1], i - 1, sumlist)
        # looplen = i-1 - checklist[A] + 1
        # looptimes = (N - checklist[A]-1) // looplen
        # ans += (sumlist[i-1] - sumlist[checklist[A]-1] )* looptimes
        # ans += sumlist[(N-checklist[A]) % looplen + checklist[A]-1]
        # print(f'loop end: {looplen}, {looptimes}')
        break
    elif A == 0:
        ans = sumlist[i - 1]
        break
    else:
        checklist[A - 1] = i
        sumlist.append(sumlist[-1] + A)
else:
    ans = sumlist[-1]

print(ans)
