t = 0
l = 'abcdefghijklmnopqrstuvwxyz'
key = {}
for i in l:
    key[i] = 0
a = int(input())
b = input()
for i in b:
    if i in l:
        key[i] += 1
    else:
        if not key[i.lower()]:
            t += 1
        else:
            key[i.lower()] -= 1
print(t)
