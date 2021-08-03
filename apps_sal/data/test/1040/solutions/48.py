N = int(input())
S = input()
a = ""
for i in range(N):
    a += S[i]
    if len(a) >= 3 and a[-3] + a[-2] + a[-1] == 'fox':
        a = a[:-3]
print(len(a))
