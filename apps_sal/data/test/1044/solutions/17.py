n = int(input())
arr = list(map(int, input().split()))
win = 2 # who wins
turn = 1
for i in range(n):
    if arr[i] != 1:
        if arr[i] % 2 == 1:
            print(3 - turn)
        else:
            turn = 3 - turn
            print(3 - turn)            
    else:
        print(3 - turn)
