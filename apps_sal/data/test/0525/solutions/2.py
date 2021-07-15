for _ in range(int(input())):
    N =int(input())
    List = [int(x) for x in input().split()]
    if(List.count(List[0]) == N):
        print(N)
    else:
        print(1)
