n = int(input())
s = '<3' + '<3'.join([input() for i in range(n)]) + '<3'
res = input()
k = 0
for c in res:
    if len(s)>k and s[k] == c:
        k+=1
if len(s)>k:
    print("no")
else:
    print("yes")
