import sys

def str_to_int(ch):
	if ch =='A':
		return 0
	if ch =='B':
		return 1
	if ch =='C':
		return 2
def int_to_str(ch):
	if ch ==0:
		return 'A'
	if ch ==1:
		return 'B'
	if ch ==2:
		return 'C'

N, A, B, C = list(map(int, input().split()))
ABC =[0, 0, 0]
ABC[0] = A
ABC[1] = B
ABC[2] = C

ops = []
for _ in range(N):
	l =list(map(str_to_int, list(input())))
	ops.append(l)

if sum(ABC) == 0:
	print("No")
	return

ans = []
for idx, op in enumerate(ops):
	n0 = ABC[op[0]]
	n1 = ABC[op[1]]
	if n0 == 0 and n1 == 0:
		print("No")
		return
	elif n1 == 0:
		inc = op[1]
		dec = op[0]
	elif n0 == 0:
		inc = op[0]
		dec = op[1]
	elif idx +1 < len(ops) and op[0] in ops[idx+1]:
		inc = op[0]
		dec = op[1]
	else:
		inc = op[1]
		dec = op[0]
	ans.append(inc)
	ABC[dec]-=1
	ABC[inc]+=1
print("Yes")
for i in map(int_to_str, ans):
	print(i)
return


