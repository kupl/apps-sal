n,d = map(int,input().split())
arr = []
for i in range(d):
    arr.append(input())

def check(s):
    fail = 0
    for x in s:
        if(x=='0'):
            fail = 1
    return fail

pres = 0
max = 0
for x in arr:
    if(check(x)):
        pres += 1
    else:
        if(max<pres):
            max = pres
        pres = 0
if(max<pres):
    max = pres
print(max)
