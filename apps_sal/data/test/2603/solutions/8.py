from math import gcd
for _ in range(int(input())):
    N = int(input())
    List = [int(x) for x in input().split()]
    Sorted = List.copy()
    Sorted.sort()
    Min = Sorted[0]
    flag = 0
    for i in range(N):
        if(List[i] != Sorted[i]):
            if(gcd(List[i],Min) == Min):
                continue
            else:
                flag = 1
                break
    if(flag):
        print("NO")
    else:
        print("YES")
