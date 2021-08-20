import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    number = str(int(input()))
    if N % 2:
        for i in range(N):
            if i % 2 == 0 and int(number[i]) % 2:
                print(1)
                break
        else:
            print(2)
    else:
        for i in range(N):
            if i % 2 and int(number[i]) % 2 == 0:
                print(2)
                break
        else:
            print(1)
