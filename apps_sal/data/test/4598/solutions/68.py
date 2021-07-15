from sys import stdin
input = stdin.readline

N = int(input())

if N % 2 == 1:
    print(N * (N+1)//2)
else:
    print((N+1) * N//2)
