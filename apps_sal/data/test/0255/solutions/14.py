n = int(input())
ai = sorted(list(map(int, input().split())))
m = int(input())
bi = sorted(list(map(int, input().split())))
i = 0
j = 0
ni = 0
while i < n and j < m:
    if ai[i] < bi[j] - 1:
        while i < n and ai[i] < bi[j] - 1:
            i += 1
    elif ai[i] - 1 > bi[j]:
        while j < m and ai[i] - 1 > bi[j]:
            j += 1
    if i < n and j < m and (ai[i] == bi[j] or ai[i] - 1 == bi[j] or ai[i] == bi[j] - 1):
        ni += 1
        i += 1
        j += 1
print(ni)
