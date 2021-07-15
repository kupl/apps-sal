n = int(input())
a = list(map(int, input().split()))
cnt_plus, cnt_minus = 0, 0
cur_plus, cur_minus = 0, 0
for v in a:
	if v > 0:
		cur_plus += 1
	else:
		cur_minus, cur_plus = cur_plus + 1, cur_minus		
	cnt_plus += cur_plus
	cnt_minus += cur_minus
print(cnt_minus, cnt_plus)

