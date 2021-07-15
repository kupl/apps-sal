t = int(input())
for test in range(t):
    n,k = [int(i) for i in input().split()]
    tab = [["0" for c in range(n)] for r in range(n)]
    row = 0
    col = 0
    while k>0:
        tab[row][col] = "1"
        row = (row+1)%n
        col += 1
        if col==n:
            col = 0
            row = (row+1)%n
        k -= 1
    if col==0:
        print(0)
    else:
        print(2)
    for row in range(n):
        print(''.join(tab[row]))
