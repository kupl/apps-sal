l = list(map(int,list(input())))
print(max(l))
ans = []
while l.count(0) != len(l):
    k = ['0' for i in range(len(l))]
    for i in range(len(l)):
        if l[i] != 0:
            l[i] -= 1
            k[i] = '1'
    ans.append(str(int(''.join(k))))
print(' '.join(ans))

