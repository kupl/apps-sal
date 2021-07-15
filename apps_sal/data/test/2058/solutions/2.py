import math


#n, s = tuple(map(int, input().split()))
#floors = [0 for i in range(s + 1)]

#for i in range(n):
#    floor, time = tuple(map(int, input().split()))
#    floors[floor] = max(floors[floor], time)

#res = s
#for i in range(s + 1):
#    res = max(res, floors[i] + i)

#print(res)

a = input()
b = input()
shift = [0]
for i in range(len(b) - len(a) + 1):
    shift[0] += int(b[i])
for i in range(len(a) - 1):
    shift.append(shift[i] - int(b[i]) + int(b[len(b) - len(a) + i + 1]))

res = 0
for i in range(len(a)):
    if a[i] == '0':
        res += shift[i]
    else:
        res += len(b) - len(a) + 1 - shift[i]
print(res)


