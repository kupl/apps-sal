t = int(input())
while t:
    t -= 1
    n = input()
    a = [int(i) for i in input().split()]
    fb = -1
    lb = -1
    c = 0
    for i in range(len(a)):
        if a[i] == 1:
            if fb == -1:
                fb = i
            lb = i
            c += 1
    print(lb - fb - c + 1)
