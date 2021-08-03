s = hex(int(input()))[2:].upper()
x = 0
x += s.count('0')
x += s.count('4')
x += s.count('6')
x += s.count('8') << 1
x += s.count('9')
x += s.count('A')
x += s.count('B') << 1
x += s.count('D')
print(x)
