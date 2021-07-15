from collections import Counter

def main():
    n=int(input())
    lst=list(map(int,input().split()))
    lst1=Counter([i+x for i,x in enumerate(lst)])
    lst2=Counter([i-x for i,x in enumerate(lst)])
    sm=0
    for x in lst1:
        if x in lst2:
            sm+=lst1[x]*lst2[x]
    print(sm)

main()
