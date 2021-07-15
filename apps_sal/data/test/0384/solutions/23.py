n = input()
s = input().split('W')
n = 0
res = ''
for i in s:
    if len(i) > 0:
        n += 1
        res += "{} ".format(len(i))
print(n)
if res:
    print(res)

