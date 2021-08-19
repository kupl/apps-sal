#!/usr/bin/env python3
s = input()
len_s = len(s)

text = ''
for i in range(len_s):
    if s[i] == '0':
        text += '0'
    elif s[i] == '1':
        text += '1'
    else:
        if text == '':
            pass
        else:
            text = text[:-1]
print(text)
