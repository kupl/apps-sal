n, m = [int(x) for x in input().split()]
arr = []
turn = []
for i in range(n):
    turn.append([None] * m)

for i in range(m):
    arr.append(list(input()))
    
for i in range(m):
    for j in range(n):
        turn[j][i] = arr[i][n - j - 1]

s = []
for i in range(n):
    s.append(list(turn[i]))
#------------------------------------------


for i in range(m):
    for j in range(n):
        turn[j][i] = s[n - j - 1][i]


for i in range(n):
    for k in range(2):
        for j in range(m):
            print(turn[i][j] * 2, end="")
        print()
            

    

