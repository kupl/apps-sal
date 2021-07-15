vowels = ['a', 'e', 'i', 'o', 'u']

a, b = input(), input()

if len(a) != len(b):
    print('No')
else:
    ok = True
    for i in range(len(a)):
        ok = ok and ((a[i] in vowels) == (b[i] in vowels))
    if ok:
        print('Yes')
    else:
        print('No')
