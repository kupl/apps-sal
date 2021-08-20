s = input()
num = s.count('g') - s.count('p')
print((num - len(s) % 2) // 2)
