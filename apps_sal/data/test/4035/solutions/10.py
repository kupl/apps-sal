A,B = list(map(int,input().split()))
ans = -1
for i in range(10**3 + 1):
    if (i*8)//100 == A and (i*10)//100 == B:
        ans = i
        break

print(ans)

