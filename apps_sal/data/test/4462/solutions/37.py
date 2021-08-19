n = int(input())
A = list(map(int, input().split()))
ans = 'No'
c1 = c2 = c4 = 0
for a in A:
    if a % 4 == 0:
        c4 += 1
    elif a % 2 == 0:
        c2 += 1
    else:
        c1 += 1
if c4 == 0 and c1 > 0:
    ans = 'No'
elif c1 <= c4 + (c2 == 0):
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
