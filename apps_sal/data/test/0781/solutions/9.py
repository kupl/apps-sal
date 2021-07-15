cnt = 0
for i in range(8):
    s = input()
    if s == 'WB'*4 or s == 'BW'*4:
        cnt += 1
if cnt == 8: 
    print('YES')
else:
    print('NO')


