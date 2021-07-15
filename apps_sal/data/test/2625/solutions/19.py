n = int(input())
for i in range(n):
    k,x = map(int, input().split())
    print(x + 9*(k-1))
