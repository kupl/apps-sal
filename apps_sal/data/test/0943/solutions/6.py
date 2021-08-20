n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
s = sum(arr)
if s % 2 == 0:
    print(s)
else:
    c = -1
    for v in arr:
        if v % 2 == 1:
            c = v
            break
    if c == -1:
        print(0)
    else:
        print(s - c)
