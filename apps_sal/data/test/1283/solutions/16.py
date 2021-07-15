#This code sucks, you know it and I know it.  
#Move on and call me an idiot later.

n, k = list(map(int, input().split()))
l = [input() for i in range(n)]
d = [[0 for i in range(n)] for i in range(n)]
s = '.' * k
md = 0
for i in range(n):
    for j in range(n):
        if l[i][j:j+k] == s:
            for ii in range(k):
                d[i][j + ii] += 1

for i in range(n):
    for j in range(n):
        if l[j][i] == '.' and j + k <= n:
            jj = j
            while(jj < j + k):
                if l[jj][i] == '.':
                    d[jj][i] += 1
                else:
                    jj -= 1
                    while(jj >= j):
                        d[jj][i] -= 1
                        jj -= 1
                    break
                
                jj += 1

md = max(list(map(max, d)))
for i in range(n):
    for j in range(n):
        if d[i][j] == md:
            print(i+1, j+1)
            return

