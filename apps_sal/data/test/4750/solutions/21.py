
t = int(input())

for _ in range(t):
    a, b, c, d = list(map(int, input().split(" ")))
    if(a != d):
        print(a, d)
    else:
        print(a, d - 1)
