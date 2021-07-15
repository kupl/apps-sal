import sys
input = sys.stdin.readline

fw = "First"
sw = "Second"
t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    if n % 2 == 1:
        print(sw)
    else:
        A.sort()
        ng = 0
        for i in range(n//2):
            if A[2*i] != A[2*i+1]:
                ng = 1
                break
        print(sw if ng == 0 else fw)
