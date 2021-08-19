n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
if sum(a) != sum(b):
    print(-1)
else:
    L = 0
    while a or b:
        if a[-1] == b[-1]:
            del a[-1]
            del b[-1]
            L += 1
        elif a[-1] < b[-1]:
            a[-2] += a[-1]
            del a[-1]
        else:
            b[-2] += b[-1]
            del b[-1]
    print(L)
