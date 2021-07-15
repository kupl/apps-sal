def main():
	s = ""
	i = 1
	while(len(s) <= 1009):
		s += str(i)
		i += 1
	print(s[int(input()) - 1])



main()
