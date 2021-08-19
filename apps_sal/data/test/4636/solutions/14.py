import sys
input = sys.stdin.readline
for t in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    a = l.pop(0)
    b = 0
    move = 0
    ad = a
    bd = 0
    able = True
    count = 1
    while l:
        bd = 0
        while bd <= ad:
            bd += l.pop(-1)
            if l == []:
                able = False
                break
        b += bd
        count += 1
        if able == False:
            break
        ad = 0
        while ad <= bd:
            ad += l.pop(0)
            if l == []:
                able = False
                break
        a += ad
        count += 1
        if able == False:
            break
    print(count, a, b)
