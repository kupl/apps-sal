s = input()
t = input()
print(sum([s[i] != t[i] for i in range(len(s))]))
