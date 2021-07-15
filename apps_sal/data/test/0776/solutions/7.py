a, b, c = map(int, input().split())
m = int(input())
usbMice = []
ps2Mice = []
for i in range(m):
	price, mouseType = input().split()
	if mouseType == 'USB':
		usbMice.append(int(price))
	else:
		ps2Mice.append(int(price))

usbMice.sort()
ps2Mice.sort()

quantity = 0
totalPrice = 0

aOk = min(a, len(usbMice))
bOk = min(b, len(ps2Mice))

totalPrice += sum(usbMice[:aOk])
totalPrice += sum(ps2Mice[:bOk])

mixMice = usbMice[aOk:] + ps2Mice[bOk:]

mixMice.sort()

cOk = min(c, len(mixMice))

totalPrice += sum(mixMice[:cOk])
quantity = aOk + bOk + cOk

print(quantity, totalPrice)
