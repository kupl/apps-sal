t=int(input())
for i in range(t):
    n, a, b =map(int, input().split())
    r=''
    for j in range(n):
        r+=chr(97+j%b)
    print(r)
