k = int(input())
s = input()
if len(s) <= k:
    print(s)
else:
    for i in range(k):
        print(s[i], end='')
    print('...')
