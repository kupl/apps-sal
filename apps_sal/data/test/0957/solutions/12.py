s = str(input())
j = 0
ss = 'heidi#'
for i in s:
    if i == ss[j]:
        j += 1
print ('YES' if j == 5 else 'NO')
