ans = 'YES'
for i in range(8):
    t = input()
    if t[0] == 'B':
        if t.count('BW') != 4:
            ans = 'NO'
            break
    else:
        if t.count('WB') != 4:
            ans = 'NO'
            break 
print(ans)
