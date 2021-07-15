n = int(input())


chess_start = 0
chess_end = 100000000000
prog_start = 0
prog_end = 100000000000
for i in range(n):
	s, f = list(map(int, input().split()))
	if s > chess_start:
		chess_start = s
	if f < chess_end:
		chess_end = f
		
m = int(input())
for i in range(m):
	s, f = list(map(int, input().split()))
	if s > prog_start:
		prog_start = s
	if f < prog_end:
		prog_end = f

chessfirst = prog_start - chess_end

progfirst = chess_start - prog_end

print(max(0, chessfirst, progfirst))



