import sys;
def transform(c):
	if c == '.': return 0;
	if c == '#': return 1;
	return 2;

def take_care(board,n,m):
	if n + 2 >= N:
		return;
	if m + 2 >= M:
		return;
	if board[n][m+1] == 0 or board[n][m+2] == 0 or board[n+1][m] == 0 or board[n+1][m+2] == 0 or board[n+2][m] == 0 or board[n+2][m+1] == 0 or board[n+2][m+2] == 0:
		return;
	board[n][m] = 2
	board[n][m+1] = 2
	board[n][m+2] = 2
	board[n+1][m] = 2
	board[n+1][m+2] = 2
	board[n+2][m] = 2
	board[n+2][m+1] = 2
	board[n+2][m+2] = 2
	return False,board;

N,M = [int(i) for i in input().strip().split()];
board = [];
for n in range(N):
	row = input().strip();
	row = [ transform(c) for c in row];
	board.append(row);
#print('board = ');
#print(board);
for n in range(N):
	for m in range(M):
		take_care(board,n,m);
for row in board:
	if 1 in row:
		print('NO');
		return;
print('YES');

