gl = ['a', 'e', 'i', 'o', 'u']
s1 = input()
s2 = input()
if len(s1) != len(s2):
    print('No')
else:
    ok = True
    for i in range(len(s1)):
        if (s1[i] in gl and s2[i] not in gl) or (s1[i] not in gl and s2[i] in gl):
            ok = False
    if ok:
        print('Yes')
    else:
        print('No')

