s = input()
N = len(s)
if N == 2:
    if s[0] == s[1]:
        print('1 2')
        return
    else:
        print('-1 -1')
        return
for i in range(N - 2):
    if s[i] == s[i + 1] or s[i] == s[i + 2]:
        print((i + 1, i + 3))
        return
if s[-1] == s[-2]:
    print((N - 2, N))
    return
print('-1 -1')
