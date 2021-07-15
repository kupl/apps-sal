s = input()
s0 = s[::2]
s1 = s[1::2]
print(s1.count('g') - s0.count('p'))
