n = int(input())
al = list(map(int, input().split()))
count2 = 0
count4 = 0
for a in al:
    if a % 4 == 0:
        count4 += 1
    elif a % 2 == 0:
        count2 += 1
v = count2 // 2
n -= v * 2
if count4 >= n // 2:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
