import sys

n = int(input())

if n <= 2:
    print(-1)
    return
elif n == 3:
    board = [[4, 5, 8], [3, 2, 6], [1, 9, 7]]
else:
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    curr = 1
    
    # Do a J-walk
    for i in range(1, n - 1):
        board[0][i] = curr
        curr += 1
    
    for i in range(n - 1):
        board[1][n - 2 - i] = curr
        curr += 1

    # Move to the side
    board[2][0] = curr
    curr += 1

    # Fill the right
    for i in range(2, n):
        board[i][n - 1] = curr
        curr += 1

    # Half-trap
    board[1][n - 1] = curr
    curr += 1
    board[0][n - 1] = curr
    curr += 1

    # Teleport spot (rook moves here, queen skips)
    board[0][0] = n * n

    # Opposite corner (this is where the queen skips to, and where the rook escapes)
    board[n - 1][0] = curr
    curr += 1

    # Rest of trap side
    for i in range(3, n - 1):
        board[i][0] = curr
        curr += 1
        
    # The non-filled area should now form a square

    # Right side
    for i in range(2, n):
        board[i][n - 2] = curr
        curr += 1

    # Vertical snake-fill to the left
    bottom = True
    for i in range(n - 3, 0, -1):
        if bottom:
            for j in range(n - 1, 1, -1):
                board[j][i] = curr
                curr += 1
        else:
            for j in range(2, n):
                board[j][i] = curr
                curr += 1
            
        bottom = not bottom
    
for r in board:
    print(" ".join(map(str, r)))

