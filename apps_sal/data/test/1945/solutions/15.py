inCount = int(input())
a = {}
for i in range(inCount):
    curStr1, curStr2 = input().split()
    if curStr1 not in a.keys():
        a[curStr2] = curStr1
    else:
        prevValue = a[curStr1]
        a.pop(curStr1)
        a[curStr2] = prevValue
print(len(a))
for key, value in a.items():
    print(value, key)
