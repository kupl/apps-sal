def is_palindrome(s):
    return s == s[::-1]

s = input()
letters = set(s)
found = False
for letter in letters:
    for i in range(len(s)+1):
        temp = s[:i] + letter + s[i:]
        if is_palindrome(temp):
            print(temp)
            found = True
            break
    if found:
        break
if not found:
    print('NA')

