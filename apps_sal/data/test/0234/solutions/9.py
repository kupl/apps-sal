def check(board):
	rows, cols = len(board), len(board[0])

	duv = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
	for i, row in enumerate(board):
		for j, x in enumerate(row):
			if '0' <= x <= '8':
				cnt = 0
				for du, dv in duv:
					u, v = i + du, j + dv
					if 0 <= u < rows and 0 <= v < cols and board[u][v] == '*':
						cnt += 1
				if int(x) != cnt:
					return False
	return True

def main():
	rows, cols = map(int, input().split())
	
	board = []
	for _ in range(rows):
		line = input().strip()

		board.append(['0' if c == '.' else c for c in line])


	if check(board):
		print('YES')
	else:
		print('NO')

def __starting_point():
	main()
__starting_point()
