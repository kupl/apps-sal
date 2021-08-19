(a, b) = (input().split(':'), input().split(':'))
a = int(a[0]) * 60 + int(a[1])
b = int(b[0]) * 60 + int(b[1])
t = (a + b) // 2
print(str(t // 60).rjust(2, '0') + ':' + str(t % 60).rjust(2, '0'))
