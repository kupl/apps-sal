#print('HARE KRISHNA')
def I():
    return int(input())


def IL():
    return list(map(int, input().split()))


def IM():
    return map(int, input().split())


def IS():
    return input()


def ISL():
    return list(input())


n = I()
l = IL()
maxi1 = 0
for i in range(1, n):
    if l[i] != l[0]:
        maxi1 = i
maxi2 = 0
for i in range(n - 2, -1, -1):
    if l[i] != l[n - 1]:
        maxi2 = i
maxi2 = (n - 1 - maxi2)
print(max(maxi1, maxi2))
