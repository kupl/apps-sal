for _ in range(int(input())):
    n = int(input())
    l = [int(i) if int(i) <= 2048 else 0 for i in input().split()]
    if(sum(l)>=2048):
        print("YES")
    else:
        print("NO")
