n = int(input())
a = [input()]
for i in range(n - 1):
    tmp = input()
    if not tmp in a and tmp[0] == a[-1][-1]:
        a.append(tmp)
    else:
        break
if len(a) == n:
    print('Yes')
else:
    print('No')
