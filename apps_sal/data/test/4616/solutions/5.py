s = list(input())
a = ''
b = s.pop(0)
c = s.pop()
a += b
a += str(len(s))
a += c
print(a)
