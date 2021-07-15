def Replacing():
    N = int(input())
    A = list(map(int,input().split()))
    lis = [0 for i in range(10 ** 5)]
    res = 0
    for i in A:
        lis[i-1] += 1
        res += i
    
    Q = int(input())
    for i in range(Q):
        b, c = list(map(int,input().split()))
        num = lis[b-1]
        res += (c - b) * num
        lis[b-1] = 0
        lis[c-1] += num
        print(res)
        
Replacing()

