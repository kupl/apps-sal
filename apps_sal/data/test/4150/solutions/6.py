import sys
n, k = list(map(int, input().split()))
l = list(map(int, input().split()))
for i in range(n):
    l[i] -= 1
taken = [0] * n
place = [0] * n
nast = [i + 1 for i in range(n)]
poprz = [i - 1 for i in range(n)]
for i in range(n):
    place[l[i]] = i
best = n - 1
turn = 2
while True:
    #print(taken, poprz, nast)
    # print(best)
    turn = 3 - turn
    p = place[best]
    pp = p
    # print(pp)
    taken[p] = turn
    for i in range(k):
        if nast[pp] < n:
            pp = nast[pp]
            taken[pp] = turn
        else:
            pp = n
            break
    # print('c')
    if pp < n:
        right = nast[pp]
    else:
        right = n
    pp = p
    for i in range(k):
        if poprz[pp] >= 0:
            pp = poprz[pp]
            taken[pp] = turn
        else:
            pp = -1
            break
    if pp >= 0:
        left = poprz[pp]
    else:
        left = -1
    # print(left,right)
    # print("c")
    if left > -1:
        nast[left] = right
    if right < n:
        poprz[right] = left
    while True:
        if best < 0:
            for f in taken:
                print(f, end="")
            return
        if taken[place[best]] != 0:
            best -= 1
        else:
            break
