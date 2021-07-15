def ans123(A:int, B:int, C:int, D:int, E:int):
    serch_list=[A,B,C,D,E]
    number=0
    minnum=0
    min=1
    if A%10==0 and B%10==0 and C%10==0 and D%10==0 and E%10==0:
        return A+B+C+D+E
    else:
     for i in range(5):
        x=serch_list[i]
        if x%10!=0 and -(-x//10)*10-x>=min:
            min=-(-x//10)*10-x
            number=i
            minnum=x
     del serch_list[number]
    return -(-serch_list[0]//10)*10+-(-serch_list[1]//10)*10+-(-serch_list[2]//10)*10+-(-serch_list[3]//10)*10+minnum

A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
print((ans123(A,B,C,D,E)))

