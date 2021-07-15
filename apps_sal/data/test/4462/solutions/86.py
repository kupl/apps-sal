N = int(input())
lsa = list(map(int,input().split()))
ans = 'Yes'
i4 = 0
i2 = 0
i1 = 0
for i in range(N):
    if lsa[i] % 4 == 0:
        i4 += 1
    elif lsa[i] % 2 == 0:
        i2 += 1
    else:
        i1 += 1
if i4+1 < i1:
    ans = 'No'
elif i2%2 == 1 and i4+1 == i1:
    ans = 'No'
print(ans)
