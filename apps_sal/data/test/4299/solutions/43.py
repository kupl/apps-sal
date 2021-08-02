l1 = [2, 4, 5, 7, 9]
l2 = [0, 1, 6, 8]
n = input()
last = int(n[-1:])
if(last in l1):
    print('hon')
elif(last in l2):
    print('pon')
else:
    print('bon')
