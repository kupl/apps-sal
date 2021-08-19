array = input('').split(' ')
totalsum = 0
summ = 0
n = array[0]
d = array[1]
listfromsmallesttolargest = input('').split(' ')
m = int(input(''))
for u in range(0, len(listfromsmallesttolargest)):
    summ = summ + int(listfromsmallesttolargest[u])
listfromsmallesttolargest = [int(x) for x in listfromsmallesttolargest]
listfromsmallesttolargest.sort()
if int(m) >= int(n):
    print(summ - int(d) * (int(m) - int(n)))
if int(m) < int(n):
    for bub in range(0, int(m)):
        totalsum = totalsum + int(listfromsmallesttolargest[bub])
    print(totalsum)
