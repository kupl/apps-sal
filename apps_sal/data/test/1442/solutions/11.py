n,s = [int(x) for x in input().split()]
buy_dict = {}
sell_dict = {}
for i in range(n):
	chtype,pi,di = input().split()
	pi = int(pi)
	di = int(di)
	if chtype=='B':
		buy_dict[pi] = buy_dict.get(pi,0)+di
	else:
		sell_dict[pi] = sell_dict.get(pi,0)+di
buy_list = sorted(list(buy_dict.items()),reverse=True)[:s]
sell_list = reversed(sorted(sell_dict.items())[:s])
for pi,qi in sell_list:
	print('S',pi,qi)
for pi,qi in buy_list:
	print('B',pi,qi)

