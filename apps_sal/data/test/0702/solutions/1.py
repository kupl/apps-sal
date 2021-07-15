n = int(input())
board = [[c for c in input()] for _ in range(n)]
# x = row
for x in range(n):
    # y = col
    for y in range(n):
        if board[x][y] == ".":
            if y == (n-1) or x >= (n-2) or y==0:
                print ("NO")
                return
            board[x][y] = "#"
            if board[x+1][y-1] == "#":
                print ("NO")
                return
            board[x+1][y-1] = "#"
            if board[x+1][y] == "#":
                print ("NO")
                return
            board[x+1][y] = "#"
            if board[x+1][y+1] == "#":
                print ("NO")
                return
            board[x+1][y+1] = "#"
            if board[x+2][y] == "#":
                print ("NO")
                return
            board[x+2][y] = "#"
print ("YES")
