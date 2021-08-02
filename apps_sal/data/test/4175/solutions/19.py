N = int(input())
l = [str(input())]
for i in range(N - 1):
    w = str(input())
    if w in l:
        print('No')
        return
    elif l[-1][-1] != w[0]:
        print('No')
        return
    else:
        l.append(w)
print('Yes')
