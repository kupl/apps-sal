a = input()
b = input()

length = len(a) - len(b) + 1

ans = []
for i in range(length):
    A = list('?' * i + b + '?' * (length - i - 1))
    flag = True
    for j in range(len(a)):
        if a[j] == '?' or a[j] == A[j]:
            pass
        elif a[j] != '?' and A[j] == '?':
            A[j] = a[j]
        else:
            flag = False
    if flag:
        ans.append(''.join(A).replace('?', 'a'))

if ans:
    ans.sort()
    print(ans[0])
else:
    print('UNRESTORABLE')
