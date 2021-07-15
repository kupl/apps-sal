def main():
	strn = input()
	n = int(strn)
	if n >= 0:
		print(n)
	else:
		del_last = int(strn[:-1])
		del_pult = int(strn[:-2] + strn[-1])
		print(max(n, del_pult, del_last))

def __starting_point():
	main()
__starting_point()
