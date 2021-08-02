a = int(input())
for i in range(a):
    b = int(input())
    l = list(map(int, input().split()))
    print((sum(l) + b - 1) // b)
