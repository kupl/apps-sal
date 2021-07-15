n,b,a = list(map(int,input().split()))
si = list(map(int,input().split()))
a2 = a
ans = n
for i in range(n):
    if b != 0:
        if a2 == a:
            a2 -= 1
        else:
            if a2 != 0:
                if si[i] == 1:
                    b -= 1
                    a2 += 1
                else:
                    a2 -= 1
            else:
                b -= 1
                if si[i] == 1:
                    a2 += 1
    else:
        if a2 == 0:
            ans = i
            break
        a2 -= 1
print(ans)
        

