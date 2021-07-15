[n, m] = list(map(int,input().split()))
solutions = 0
if m < n:
    temp = m
    m = n
    n = temp
if n >= 3:
    if n%2==1 and m%2 == 1:
        solutions = n*m-1
    else:
        solutions = n*m
if n == 1:
    if m <= 3:
        solutions = 0
    if m%6 == 0:
        solutions = m
    if m% 6 == 1 or m%6 == 5:
        solutions = m - 1
        #no need to write m*n as n = 1 so m shld suffice
    if m%6 == 2 or m%6 == 4:
        solutions = m - 2
    if m%6 == 3:
        solutions = m - 3
if n == 2:
    if m <= 2 :
        solutions = 0
    elif m <= 3:
        solutions = m*n-2
    elif m <=6:
        solutions = m*n
    elif m <= 7:
        solutions = m*n-2
    else:
        solutions = m*n
print (solutions)
