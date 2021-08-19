#n = int(input())
d, n = list(map(int, input().split()))
#al = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]

if n == 100:
    print((101 * (100**d)))
else:
    print((n * (100**d)))
