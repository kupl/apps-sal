s = input()
print(max(list(map(int, [s, s[0:-1], s[0:-2] + s[-1]]))))
