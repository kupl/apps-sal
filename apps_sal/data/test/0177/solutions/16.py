s = ''
for i in range(1, 100000000):
    s += str(i)
    if len(s) >= 11000:
        break
print(s[int(input()) - 1])
