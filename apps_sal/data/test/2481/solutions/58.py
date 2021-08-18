def main():
    H, W = [int(x) for x in input().split(" ")]
    C = []
    for i in range(10):
        c = [int(m) for m in input().split(" ")]
        C.append(c)
    A = [0] * 10
    for i in range(H):
        a = [int(m) for m in input().split(" ")]
        for j in range(W):
            if a[j] != -1:
                A[a[j]] += 1

    MP = [[C[i][1] for i in range(10)]]
    for i in range(9):
        MP.append([min([(C[k][j] + MP[-1][j]) for j in range(10)]) for k in range(10)])

    minMP = [10000] * 10
    for i in range(len(MP)):
        for j in range(len(MP[i])):
            minMP[j] = min([minMP[j], MP[i][j]])
    print(sum([p * q for (p, q) in zip(A, minMP)]))


main()
