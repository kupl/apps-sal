import copy
b = []
a = []
rezult = ''
n = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(1, m + 1):
    k, pos = list(map(int, input().split()))
    b = copy.deepcopy(a)
    b.reverse()
    for j in range(1, n - k + 1):
        b.remove(min(b))
    b.reverse()
    rezult = rezult + '\n' + str(b[pos - 1])
print(rezult)
