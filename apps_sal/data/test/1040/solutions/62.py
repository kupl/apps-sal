N = int(input())
S = input()
a = ''
for i in range(N):
    a += S[i]
    if 'fox' == a[-3:]:
        a = a[:-3]
print(len(a))
