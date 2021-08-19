n = int(input())
a = list(map(int, input().split()))
four = 0
two = 0
other = 0
for i in a:
    if i % 4 == 0:
        four += 1
    elif i % 2 == 0:
        two += 1
    else:
        other += 1
ans = 'No'
other += two % 2
if four + 1 >= other:
    ans = 'Yes'
print(ans)
