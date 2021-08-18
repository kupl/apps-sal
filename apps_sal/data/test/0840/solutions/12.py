class Ingred:
    def __init__(self, i, a, b):
        self.index = i
        self.needed = a
        self.given = b
        self.possbl = int(b / a)

    def __repr__(self):
        return "[" + str(self.needed) + "," + str(self.given) + "," + str(self.possbl) + "]"


def per(obj):
    return obj.possbl


def findIndex(x, arr):
    start = 0
    end = len(arr) - 1
    if arr[0].possbl >= x:
        return -1
    if arr[-1].possbl < x:
        return end
    while True:
        ind = int((start + end) / 2)
        if arr[ind].possbl < x:
            start = ind
            if ind < len(arr) - 1 and arr[ind + 1].possbl >= x:
                return ind
        else:
            end = ind

        if ind == len(arr) - 1:
            return ind


def xTimes(x, arr, needed, given, magic):
    ind = findIndex(x, arr)
    if ind == -1:
        return True
    deficit = needed[ind] * x - given[ind]
    if deficit > magic:
        return False
    return True


inf = list(map(int, input().split()))
n = inf[0]
k = inf[1]
temp = list(map(int, input().split()))
tmp = list(map(int, input().split()))
given = [0] * n
needed = [0] * n
array = [None] * n
for i in range(n):
    array[i] = Ingred(i, temp[i], tmp[i])
array = sorted(array, key=per)
for i in range(n):
    needed[i] = needed[i - 1] + array[i].needed
    given[i] = given[i - 1] + array[i].given
start = 0
end = 4000000009
x = start
dic = {}
while True:
    p = xTimes(x, array, needed, given, k)
    dic[x] = True
    if p:
        start = x
    else:
        end = x

    x = int((start + end) / 2)
    try:
        dic[x]
        break
    except:
        damn = 0
print(x)
