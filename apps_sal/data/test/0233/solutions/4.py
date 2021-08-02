mc = 0
cc = 0
for i in range(int(input())):
    m, c = list(map(int, input().split()))
    if m > c:
        mc += 1
    if c > m:
        cc += 1
if mc > cc:
    print('Mishka')
elif cc > mc:
    print('Chris')
else:
    print('Friendship is magic!^^')
