n = int(input())
s = input()

i = 0
to_add = 1
while i < n:
    print(s[i], end='')
    i += to_add
    to_add += 1

