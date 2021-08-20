dep = dict()


def kmp(st):
    tam = len(st)
    pi = [0] * tam
    for i in range(1, tam):
        j = pi[i - 1]
        while j > 0 and st[j] != st[i]:
            j = pi[j - 1]
        if st[j] == st[i]:
            pi[i] = j + 1
        dep[pi[i]] = pi[pi[i] - 1]
    return pi


s = input()
arr = kmp(s)
points = [0] * len(s)
toimp = list()
actpi = arr[-1]
while actpi != 0:
    toimp.append(actpi)
    actpi = arr[actpi - 1]
toimp.sort()
for i in range(len(arr)):
    points[arr[i]] += 1
for i in range(len(s) - 1, 0, -1):
    if i in dep:
        points[dep[i]] += points[i]
print(len(toimp) + 1)
for i in toimp:
    print(str(i) + ' ' + str(points[i] + 1))
print(str(len(s)) + ' 1')
