n = int(input())
a = []
for i in range(n):
    _ = list(map(int, input().split()))
    a.append(_)
a = sorted(a, key=lambda x:x[2],reverse = True)

check = False
    
for i in range(101):
    for j in range(101):
        b = 0
        while b < n:
            if b == 0:
                h = abs(i - a[b][0]) + abs(j - a[b][1]) + a[b][2]
                b +=1
            else:
                de = max(h - abs(i - a[b][0]) - abs(j - a[b][1]),0)
                if de == a[b][2]:
                    b+=1
                else:
                    break
        if b == n:
            ans = str(i) + ' ' + str(j) + ' ' +str(h)
            check = True
        if check:
            break
    if check:
        break
print(ans)

