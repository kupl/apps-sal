s = input()
up, low, digit = False, False, False
for ch in s:
    if ch.isdigit():
        digit = True
    elif ch.isalpha():
        if ch.isupper():
            up = True
        else:
            low = True
if len(s) >= 5 and up and low and digit:
    print('Correct')
else:
    print('Too weak')
