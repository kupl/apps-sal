n = int(input())
a = list(map(int, input().split()))

a.sort()


def mod():
    for i in range(1, len(a)):
        if(a[i] % a[0] != 0):
            a[i] = a[i] % a[0]
        else:
            a[i] = a[0]
    a.sort()
    return a


while(a.count(a[0]) != len(a)):
    a = mod()

print(a[0])
