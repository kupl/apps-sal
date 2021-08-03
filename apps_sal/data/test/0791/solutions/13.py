n = int(input())
s = input()

c = 0
if s[0] == '0':
    c = 1
else:

    for i in range(n):
        if s[i] == '0':
            c += 1
            break
        else:
            c += 1
print(c)
