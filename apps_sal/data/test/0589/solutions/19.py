__author__ = 'Karolis'

s = input()
total = 1
was=[]
have = 10

for i in range(len(s)):
    if s[i] == '?':
        if i == 0:
            total *= 9
        else:
            total *= 10
    elif s[i] >= 'A' and s[i] <= 'J' and was.count(s[i]) == 0:
        was.append(s[i])

        if i == 0:
            total *= 9
        else:
            total *= have
        have-=1



print(total)

