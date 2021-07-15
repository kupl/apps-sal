s = input()
s = s[0] + s[2] + s[4] + s[3] + s[1]
print(str(pow(int(s), 5, 100000)).rjust(5, '0'))
