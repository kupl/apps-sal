T =  int(input())
for _ in range(T):
    N = int(input())
    A = list(range(1,N+1))
    print(2)
    while len(A) > 1:
        a = A.pop()
        b = A.pop()
        c = (a+b+1)//2
        print(a,b)
        A.append(c)

