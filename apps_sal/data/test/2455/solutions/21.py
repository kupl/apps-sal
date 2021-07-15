
n = int(input())


for _ in range(n):
    mystr = input()
    answer = []
    
    divisibles = [1,2,3,4,6,12]
    for i in divisibles:
        flag=0
        
        for j in range(0,12//i):
            columnSet = set(mystr[j::12//i])
            if len(columnSet)==1 and "X" in columnSet:
                flag=1
                break

        if flag==1:
           answer.append("{}x{}".format(i,12//i));
    print(len(answer), " ".join(answer))

