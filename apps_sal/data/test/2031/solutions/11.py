import copy
a = []
ai = []
otv = ''
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(1, m + 1):
    ai = copy.deepcopy(a)
    ai.reverse()
    k, pos = list(map(int, input().split()))
    for j in range(1, n - k + 1):
        ai.remove(min(ai))
    ai.reverse()
    otv = otv + '\n' + str(ai[pos - 1])
print(otv)
