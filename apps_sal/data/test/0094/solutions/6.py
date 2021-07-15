n = int(input())
k = input()
pos = len(k)
ans = []
while pos > 0:
    tmp = 0
    l = pos-1
    mark = l
    while l >= 0:
        a = int(k[l:pos])
        if a >= n:
            break
        else:
            if a != tmp: mark = l
            tmp = a
            l -= 1
            
    if tmp == 0:
        pos -= 1
        ans.append(0)
    else:
        pos = mark
        ans.append(tmp)

aans = 0
for i in ans[::-1]:
    aans = aans*n + i

print(aans)

