import math
_, a, b = list(map(int, input().split()))
jet = list(map(int, input().split()))


def jtd(w):
    #d = (w*a)//b
    j = (w*a)%b
    return j//a

for i in jet:
    print(int(jtd(i)), end=' ')
print()

