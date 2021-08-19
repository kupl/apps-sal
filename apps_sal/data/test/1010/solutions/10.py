n = int(input())
nuts = list(map(int, input().split()))
label = 0
if nuts.count(1):
    ans = 1
else:
    ans = 0
for i in nuts:
    if i == 1:
        if label:
            ans *= cnt
        label = 1
        cnt = 0
    if label:
        cnt += 1
print(ans)
