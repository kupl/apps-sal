3
s = input()
seat = s[-1]
n = int(s[:-1])
t = 1 + 16 * ((n - 1) // 4)
n = 1 - n % 4 % 2
t += n * 7
a = ['f', 'e', 'd', 'a', 'b', 'c']
t += a.index(seat)
print(t)
