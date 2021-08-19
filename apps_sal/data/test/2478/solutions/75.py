n = int(input())
s = input()
opens = 0
l = 0
for i in range(n):
    if s[i] == '(':
        opens += 1
    else:
        opens -= 1
        if opens < 0:
            l += 1
            opens = 0
print('(' * l + s + ')' * opens)
