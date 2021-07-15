N = int(input())
S = input()

lst = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
dct1 = {}
dct2 = {}
ans = []
for i, j in enumerate(lst, 1):
    dct1[j] = i
    dct2[i] = j
for s in list(S):
    n = dct1[s] + N
    if n >=27:
        n -= 26
    m = dct2[n]
    ans.append(m)
print(''.join(ans))
