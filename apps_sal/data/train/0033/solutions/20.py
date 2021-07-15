# 3x + 5y + 7z

t = int(input())

while t:
    t -= 1
    n = int(input())
    print(2)
    arr = [n-1,n]
    print(*arr)
    for i in range(2,n):
        arr = [n-i,n-i+2]
        print(*arr)
