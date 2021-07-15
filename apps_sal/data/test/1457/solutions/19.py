a = input()
b = input()

nIndex = 0
nSum = 0
while True :
	nRet = a.find(b, nIndex)
	if nRet == -1 :
		break;
	nSum += 1
	nIndex = nRet + len(b)
print(nSum)

