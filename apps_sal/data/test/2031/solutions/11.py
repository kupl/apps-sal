import copy
a = []
ai = []
otv = ''
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(1, m + 1):
    # print(ai)
    # print(a,'kkkk')
    ai = copy.deepcopy(a)
    ai.reverse()
    # print(ai)
    k, pos = list(map(int, input().split()))
    for j in range(1, n - k + 1):
        # print(min(ai))
        ai.remove(min(ai))
    ai.reverse()
    otv = otv + '\n' + str(ai[pos - 1])
print(otv)
