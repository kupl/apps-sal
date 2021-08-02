# cook your dish here

li = list(map(int, input().split()))
if li[0] - 1 < 0:
    print((li[1] // li[2]) + 1)
else:
    print((li[1] // li[2]) - (li[0] - 1) // li[2])
