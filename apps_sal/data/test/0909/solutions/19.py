a = int(input())
b = int(input())
c = int(input())
ch1 = a + b + c
ch2 = (a + b) * c
ch3 = a * (b + c)
ch4 = a * b * c
ch5 = a + b * c
ch6 = a * b + c
print(max(ch1, ch2, ch3, ch4, ch5, ch6))
