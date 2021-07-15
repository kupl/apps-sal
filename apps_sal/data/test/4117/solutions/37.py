def main():
    n = int(input())
    s = input()
    l = s.split()
    #print(l)
    l = [int(x) for x in l]
    l.sort()
    cnt=0
    #print(l)
    for i in range(n):
        for j in range(i+1,n):
            if l[i] == l[j]:
                continue
            for k in range(j+1, n):
                if l[i] == l[k] or l[j] == l[k]:
                    continue
                #print("{},{},{}".format(l[i], l[j], l[k]))
                cnt += triangle(l[i], l[j], l[k])
    print(cnt)

def triangle(a, b, c):
    if(a + b > c and b + c > a and c + a > b):
        return 1
    else:
        return 0

def __starting_point():
    main()
__starting_point()
