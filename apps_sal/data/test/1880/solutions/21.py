n = [letter for letter in input()]
new = int(n[0] + n[2] + n[4] + n[3] + n[1]) ** 5 % 100000
k = len(str(new))
print('0' * (5 - k), new, sep = '')

