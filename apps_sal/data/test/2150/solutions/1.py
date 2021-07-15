a = int(input())
b = 0
c = list(map(int, input().split()))
for i in c:
    if i > 0:
        b += i
        print(b, end=' ')
    elif i < 0:
        print(b + i, end=' ')
    else:
        print(b, end=' ')
