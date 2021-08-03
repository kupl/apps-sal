n = int(input())
a = '<3'
for i in range(n):
    a = a + input() + '<3'

b = input()
lenb = len(b)
for i in range(lenb):
    if not ('a' <= b[i] <= 'z' or '0' <= b[i] <= '9' or b[i] == '<' or b[i] == '>'):
        print('no')
        break
else:
    j = 0
    lena = len(a)
    for i in range(lena):
        while j < lenb and a[i] != b[j]:
            j += 1
        if j == lenb:
            print('no')
            break
        j += 1
    else:
        print('yes')
