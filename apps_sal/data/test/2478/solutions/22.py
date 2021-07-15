n = int(input())
s = input()
left = 0
right = 0
for i in range(n):
    if s[i] == '(':
        right += 1
    else:
        if right > 0:
            right -= 1
        else:
            left += 1
print((left * '(' + s + right * ')'))

