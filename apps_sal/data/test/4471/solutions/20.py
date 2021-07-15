t = int(input())
while(t):
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    rems = set()
    for i in a:
        rems.add(i%2)
    if(len(rems) == 1):
        print("YES")
    else:
        print("NO")
