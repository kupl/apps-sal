n = input()

sn = 0
for i in n:
    tmp = int(i)
    s = tmp%10
    sn += s

n = int(n)
if n%sn == 0:
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
