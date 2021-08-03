t = int(input())
for _ in range(t):
    x = int(input())
    l = list(map(int, input().split()))
    gets = True
    for z in list(reversed(l))[1:]:
        if z == 1:
            gets = not gets
        else:
            gets = True
    if gets:
        print("First")
    else:
        print("Second")
