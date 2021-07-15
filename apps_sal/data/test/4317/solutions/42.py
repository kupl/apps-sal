A, B = map(int,input().split())

cal = [A+B,A-B,A*B]
cal.sort()
print(cal[-1])
