s = input()

t, u = '', ''
for i in range(len(s)):
    t += '1' if i%2 == 0 else '0'
    u += '0' if i%2 == 0 else '1'

s = int(s, 2)
t = int(t, 2)
u = int(u, 2)
print(min(bin(s^t).count('1'), bin(s^u).count('1')))
