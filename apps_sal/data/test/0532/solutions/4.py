s = input()
alfabet = 'abcdefghijklmnopqrstuvwxyz'
rot = 0
curr = 0
for c in s:
    goto = alfabet.index(c)
    rot += min(abs(goto - curr), abs(curr + 26 - goto), abs(curr - goto - 26))
    curr = goto
print(rot)
