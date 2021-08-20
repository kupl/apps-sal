n = int(input())
s = list(map(str, input().split()))
for i in s:
    if i == 'Y':
        print('Four')
        break
else:
    print('Three')
