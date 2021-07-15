n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

def kai(x):
    c = 1
    for i in range(1,x+1):
        c *= i
    return c

def dicnum(lis):
    num = [x for x in range(1,n+1)]
    count = 1
    for i in range(n-1):
        count += num.index(lis[i])*kai(n-i-1)
        num.remove(lis[i])
    return count

print(abs(dicnum(p) - dicnum(q)))
