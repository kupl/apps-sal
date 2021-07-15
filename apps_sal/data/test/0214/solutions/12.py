a = [list(input()) for _ in range(2)]
n = 0
for i in range(len(a[0])):
    bljet = 0
    if a[0][i] == a[1][i] and a[0][i] == '0':
        
        if i > 0:
            if a[0][i-1] == '0':
                a[0][i-1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                bljet = 1
            if not bljet and a[1][i-1] == '0':
                a[1][i-1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                bljet = 1
        if i+1 < len(a[0]):
            if not bljet and a[0][i+1] == '0':
                a[0][i+1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                bljet = 1
            if not bljet and a[1][i+1] == '0':
                a[1][i+1] = 'X'
                a[0][i] = 'X'
                a[1][i] = 'X'
                bljet = 1
        #print(a[0])
        #print(a[1])
        
    if bljet:
        n += 1
print(n)

