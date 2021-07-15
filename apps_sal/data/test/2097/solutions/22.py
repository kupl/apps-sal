for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    moves = 0
    x = 0
    for i in range(n):
        if l1[i] == 0:
            l1[i] = 1
            moves+=1
        x = x + l1[i]
    if x!=0:
        print(moves)
    else:
        print(moves+1)

