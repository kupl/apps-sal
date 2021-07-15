s = input()
s = list(set(s))
s = sorted(s)
alf = [chr(i) for i in range(97,97+26)]
for i in range(26):
    if alf[i] not in s:
        print((alf[i]))
        return
        
print('None')

