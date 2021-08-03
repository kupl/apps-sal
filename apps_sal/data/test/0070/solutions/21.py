def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def n(lil):
    for i in range(len(lil), -1, -1):
        if lil[i - 1] != '0':
            return lil[:i - 1] + lil[i:]


li = input().split()
k = 0
while True:
    if int(li[0]) % (10**int(li[1])) != 0:
        li[0] = n(li[0])
        k += 1
        continue
    else:
        if li[0] == '0' * len(li[0]):
            k += (len(li[0]) - 1)
        break

print(int(k))
