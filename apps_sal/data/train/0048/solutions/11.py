import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y, k = [int(i) for i in input().split()]
    
    stick_need = k+k*y-1
    
    num_stick_trade = (stick_need+x-2)//(x-1)

    
    print(num_stick_trade+k)
