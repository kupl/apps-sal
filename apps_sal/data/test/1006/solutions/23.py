n=int(input())

board=[""]*n
c=0
for i in range(n):
    board[i]=list(input())
    
    
for i in range(1,n-1):
    for j in range(1,n-1):
        if(board[i][j]=='#' and board[i-1][j]=='#' and board[i+1][j]=='#' and board[i][j-1]=='#' and board[i][j+1]=='#'):
            board[i][j]='.'
            board[i-1][j]='.'
            board[i+1][j]='.'
            board[i][j-1]='.'
            board[i][j+1]='.'
            
            
c= sum(board[i].count('#') for i in range(n))

print ('YES') if c==0 else print('NO')
            
