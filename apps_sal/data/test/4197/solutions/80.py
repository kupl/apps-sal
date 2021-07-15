def resolve():
    n = int(input())
    a = tuple(map(int,input().split()))
    attend = [0]*n
    for i,j in enumerate(a):
        attend[j-1] = i+1
    print(*attend)
resolve()
