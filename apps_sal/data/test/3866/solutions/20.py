def prnt(j):
    for i in range(j):
        print(i,end=" ")
    print()
    return
def triplet(n):
    if n%2!=0:
        prnt(n)
        prnt(n)
        for i in range(n):
            num=i+i
            if num>=n:
                num=num-n
            print(num,end=" ")
    else:
        print("-1")
n=int(input())
triplet(n)
