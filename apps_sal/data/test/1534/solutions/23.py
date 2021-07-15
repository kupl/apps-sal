s = input()
ar = [0,0,0]
for i in s:
    if i == 'a':
        ar[2] = max(ar)+1
        ar[0] += 1
    else:
        ar[1] = max(ar[0],ar[1]) + 1
print(max(ar))  
