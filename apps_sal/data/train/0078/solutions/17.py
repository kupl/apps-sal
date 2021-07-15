def __starting_point():
    T = int(input())
    #fout = open('1194B.out', 'w')
    for _ in range(T):
        s = input().rstrip().split()
        n = int(s[0])
        m = int(s[1])
        cell = [[0 for j in range(m)] for i in range(n)]
        r = [0 for i in range(n)]
        c = [0 for j in range(m)]
        for i in range(n):
            s = input()
            for j in range(len(s)):
                cell[i][j] = s[j]
                if s[j] == '*':
                    r[i] += 1
                    c[j] += 1
        nmax = 0
        for i in range(n):
            for j in range(m):
                if r[i] + c[j] + (cell[i][j] == '.') > nmax:
                    nmax = r[i] + c[j] + (cell[i][j] == '.')
        print(str(m + n - nmax) + '\n')

__starting_point()
