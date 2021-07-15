#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

#        tmp = list([int(i) for i in (list(str(i)))])

def main():
    n,a,b = map(int,input().split())
    numbers=[]
    tmp=0

    for i in range(1,n+1):
        if i >=a and i <=b and i < 10:
            numbers.append(i)
        else:
            tmp_array=list(map(int,list(str(i))))
            if len(tmp_array) > 1:
                for j in tmp_array:
                    tmp+=j
                if tmp >=a and tmp <=b:
                    numbers.append(i)
                tmp=0
            else:
                continue
    print(sum(numbers))
            
def __starting_point():
    main()
__starting_point()
