import sys





def main():
	data = sys.stdin.readline().strip()[1:-1]
	datax = data.split(', ')
	datas = set(datax)
	if datax == ['']:
		print(0)
	else:
		print(len(datas))





main()





