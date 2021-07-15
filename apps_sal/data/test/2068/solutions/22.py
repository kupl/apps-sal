def length(arr, nowman):
    l = 1
    if nowman != 'polycarp':
        l += length(arr, arr[nowman])
    return l

rarr = {}
for i in range(int(input())):
    r = input().lower().split()
    rarr[r[0]] = r[2]

maxl = 1
for key, value in list(rarr.items()):
    l = length(rarr, rarr[key])+1
    if maxl < l:
        maxl = l

print(maxl)

