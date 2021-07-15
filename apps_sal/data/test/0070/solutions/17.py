from sys import stdin, stdout

num,k = list(map(int, stdin.readline().rstrip().split()))

numStr=str(num)
if num==0:
    print(0)
elif numStr.count('0')==0:
    print(len(numStr))
elif numStr.count('0')<k:
    print(len(numStr)-1)
else:
    numReverse=numStr[::-1]
    zeroCount=0
    deleted=0
    i=0
    while zeroCount<k:
        if numReverse[i]=='0':
            zeroCount+=1
        else:
            deleted+=1
        i+=1
    print(deleted)

