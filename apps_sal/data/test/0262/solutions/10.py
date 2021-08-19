def main():

    def magic(sq, n):
        s1 = sum(sq[0])
        for i in range(1, n):
            if s1 != sum(sq[i]):
                return False
        s2 = 0
        for i in range(n):
            s2 += sq[i][i]
        if s2 != s1:
            return False
        s2 = 0
        for i in range(n):
            s2 += sq[i][n - i - 1]
        if s2 != s1:
            return False
        for i in range(n):
            s2 = 0
            for j in range(n):
                s2 += sq[j][i]
            if s2 != s1:
                return False
        return True
    n = int(input())
    sq = [list(map(int, input().split())) for i in range(n)] + [[1]]
    for i in range(n):
        if 0 in sq[i]:
            cors = (i, sq[i].index(0))
    if cors[0] != 0:
        s = sum(sq[0])
    else:
        s = sum(sq[1])
    sq[cors[0]][cors[1]] = s - sum(sq[cors[0]])
    if magic(sq, n) and sq[cors[0]][cors[1]] >= 1:
        print(sq[cors[0]][cors[1]])
    else:
        print(-1)


main()
