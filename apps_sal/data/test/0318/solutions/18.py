sLine = input()
sSplit = sLine.split(sep=':')
nHour = int(sSplit[0])
nMinute = int(sSplit[1])
nPass = int(input())
nPass = nPass % (60 * 24)
nMinute += nPass
if nMinute >= 60 :
	x = nMinute // 60
	nMinute -= 60 * x
	nHour += x
if nHour >= 24 :
	nHour %= 24
print('{0:02d}:{1:02d}'.format(nHour, nMinute))

