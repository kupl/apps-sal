s = input()
con = [0] * 2
for i in range(4):
    if s[i] == '+':
        con[0] += 1
    else:
        con[1] += 1
print(con[0] - con[1])
