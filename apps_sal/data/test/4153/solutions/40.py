s = list(input())

length = len(s)

r = s.count('0')
b = s.count('1')

print(length - abs(r-b))
