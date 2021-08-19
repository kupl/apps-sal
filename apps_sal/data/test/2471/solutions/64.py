import sys

h, w, n = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]

dict = {}
ans = [0] * 10
ans[0] = (w - 2) * (h - 2)

for item in A:  # for every paint
    cord = list(item)
#    print("----{},{}----".format(cord[0],cord[1]))
    # update candidate
    upcand = []  # max9
    for i in range(cord[0] - 1, cord[0] + 2):
        for j in range(cord[1] - 1, cord[1] + 2):
            #            print("----({},{})----".format(i,j))
            upcand.append([i, j])
#    print(upcand)
    for cand in upcand:
        #        print(cand)
        if 1 < cand[0] < h and 1 < cand[1] < w:
            #            print(cand)
            dict[(cand[0], cand[1])] = dict.get((cand[0], cand[1]), 0) + 1
#        print(dict)
for k, v in list(dict.items()):
    ans[v] += 1
    ans[0] -= 1

for i in ans:
    print(i)
