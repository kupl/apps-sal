n = int(input())
ab = [12, 6, 4, 3, 2, 1]
lst = [list(input()) for i in range(n)]
res = [[0] for i in range(n)]
for pr in range(n):
    for elem in ab:
        for i in range(elem):
            x = 1
            for j in range(0, 12, elem):
                if lst[pr][i + j] == "O":
                    x = 0
            if x == 1 and str(12 // elem) + "x" + str(elem) not in res[pr]:
                res[pr][0] += 1
                res[pr].append(str(12 // elem) + "x" + str(elem))
for i in range(len(res)):
    print(" ".join(map(str, res[i])))
