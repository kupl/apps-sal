n = int(input())
l = list(map(int, input().split()))
last = 2
for i in l:
    if i == 1:
        print(last)
    elif i % 2 == 1:
        print(last)
    else:
        last = 2 if last == 1 else 1
        print(last)
