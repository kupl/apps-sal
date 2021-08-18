A1 = list(map(str, input().split()))
A2 = list(map(str, input().split()))
A3 = list(map(str, input().split()))
N = int(input())
for k in range(N):
    i = str(input())
    if i == A1[0]:
        A1[0] = 'OK'
    if i == A1[1]:
        A1[1] = 'OK'
    if i == A1[2]:
        A1[2] = 'OK'
    if i == A2[0]:
        A2[0] = 'OK'
    if i == A2[1]:
        A2[1] = 'OK'
    if i == A2[2]:
        A2[2] = 'OK'
    if i == A3[0]:
        A3[0] = 'OK'
    if i == A3[1]:
        A3[1] = 'OK'
    if i == A3[2]:
        A3[2] = 'OK'
if A1 == ['OK', 'OK', 'OK'] or A2 == ['OK', 'OK', 'OK'] or A3 == ['OK', 'OK', 'OK']:
    print('Yes')
    return
for i in range(3):
    if A1[i] == 'OK' and A2[i] == 'OK' and A3[i] == 'OK':
        print('Yes')
        return
if A1[0] == 'OK' and A2[1] == 'OK' and A3[2] == 'OK':
    print('Yes')
    return
if A1[2] == 'OK' and A2[1] == 'OK' and A3[0] == 'OK':
    print('Yes')
    return
print('No')
