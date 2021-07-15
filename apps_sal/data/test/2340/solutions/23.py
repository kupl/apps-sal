q = int(input())
for i in range(q):
	inp = input()
	inp_arr = inp.split(" ")
	h = int(inp_arr[0])
	n = int(inp_arr[1])
	inp_p = input()
	inp_p_arr = inp_p.split(" ")
	inp_p_arr = [int(j) for j in inp_p_arr]
	inp_p_arr.append(0)
	count = 0
	par_che = 1
	for j in range(1, n):
		if inp_p_arr[j]-inp_p_arr[j+1] == 1:
			par_che += 1
		else:
			if par_che %2==1:
				count+=1
			par_che = 1

	print(count)
