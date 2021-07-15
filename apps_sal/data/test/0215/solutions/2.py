n = int(input())
b = input()
a = ['']
for i in b:
    if ord('A') <= ord(i) <= ord('Z'):
        a.append('')
    else:
        a[-1] = a[-1] + i
a = [len(set(list(i))) for i in a]
print(max(a))
