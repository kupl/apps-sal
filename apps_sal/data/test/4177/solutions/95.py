S = input()
list_s = list(S)
for i in range(0, len(list_s)):
    list_s[i] = "x"

print(''.join(list_s))
