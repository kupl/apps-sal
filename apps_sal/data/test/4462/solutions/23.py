N = int(input())
a = list(map(int, input().split()))
sa = []
c = [0] * 4
ans = 'No'
for i in a:
    sa.append(i % 4)
for i in sa:
    c[i] += 1
if c[2] == 0:
    if c[1] + c[3] <= c[0] + 1:
        ans = 'Yes'
elif c[1] + c[3] <= c[0]:
    ans = 'Yes'
print(ans)
