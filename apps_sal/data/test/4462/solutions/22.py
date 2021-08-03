N = int(input())
a = list(map(int, input().split()))

cnt2 = 0
cnt4 = 0
cntodd = 0
for i in a:
    if i % 4 == 0:
        cnt4 += 1
    elif i % 2 == 0:
        cnt2 += 1
    else:
        cntodd += 1

if cnt2 == 0 and cnt4 + 1 >= cntodd:
    ans = 'Yes'
elif cnt4 >= cntodd:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
