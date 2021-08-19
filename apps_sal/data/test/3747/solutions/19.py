#!/usr/bin/env python3
text = input()
bolba = "Bulbasaur"
chars = {}
for i in bolba:
    chars[i] = 0
for i in text:
    if i in bolba:
        chars[i] += 1
chars['u'] = chars['u'] // 2
chars['a'] = chars['a'] // 2
print(min(chars.values()))
