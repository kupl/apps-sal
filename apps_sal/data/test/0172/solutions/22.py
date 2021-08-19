def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()


def check(li1, li2):
    result = 0
    for i in range(5):
        result += ((max(li1[i], li2[i]) - min(li1[i], li2[i])) / 2)
        if (li1[i] + li2[i]) % 2 != 0:
            print(-1)
            return
    print(int(result / 2))
    return


li1 = [0, 0, 0, 0, 0]
li2 = [0, 0, 0, 0, 0]
n = II()

ll1 = LI()
ll2 = LI()
for i in range(n):
    li1[ll1[i] - 1] += 1
    li2[ll2[i] - 1] += 1
# print(li1, li2)

check(li1, li2)
