n = int(input())
# x,y,z,t1,t2,t3=map(int,input().split())
a = list(map(int, input().split()))


def qwe(a):
    f = -1
    for i in range(len(a)):
        if a[i] - f > 1:
            return i + 1
        elif a[i] - f == 1:
            f = a[i]
    return -1


print(qwe(a))
