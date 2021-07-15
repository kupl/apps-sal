

s = input()

y = []
for i in range(1 , len(s) - 1):
    x = int(s[i - 1 : i + 2])
    y.append(abs(x - 753))
print(min(y))
