def main():
    [n, m, k] = [int(x) for x in input().split()]
    l = [int(x) for x in input().split()]
    print(result(n, m, k, l))

def result(n, m, k, l):
    f = 0
    l.sort()
    l.reverse()
    while(k<m):
        if l==[]:
            return -1
        f+=1
        k+=l[0]-1
        l=l[1:]
    return f    
def __starting_point():
    main()

__starting_point()
