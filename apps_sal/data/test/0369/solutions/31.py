n, m = list(map(int,input().split()))
s = list(input())

s.reverse()
ng = False
c = 0
ans = []
while ng == False and c < n:
    for i in range(m, 0, -1):
        if c+i < n+1 and s[c+i] == '0':
            c += i
            ans.append(str(i))
            break
        elif i == 1:
            ng = True
if ng:
    print((-1))
else:
    ans.reverse()
    print((' '.join(ans)))

