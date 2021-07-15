n=int(input())

for i in range(n):

    a=(input())

    zeroes=0
    evens=0
    summ=0

    for b in a:
        if int(b)%2 == 0: evens+=1
        if int(b)==0: zeroes+=1
        summ += int(b)

    if zeroes>0 and evens>1 and summ%3==0: print('red')
    else: print('cyan')

