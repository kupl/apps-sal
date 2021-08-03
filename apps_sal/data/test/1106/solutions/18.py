
n = int(input())
a = [int(x) for x in input().split()]
m = len(a)

sums = [0] * (m + 1)
count = 0

a.insert(0, 0)

#stack = [(0, 0)]
# while stack:
#v, s = stack.pop(0)
#sums[v] = s
##print(v+1, s)

# if 2*v+1 >= m:
# sums.append(s)
# if s > count:
#count = s
# continue

#stack.append((2*v+1, s+a[2*v+1]))
#stack.append((2*v+2, s+a[2*v+2]))

#print(sums, count)

add = 0
for i in range(m // 2 - 1, -1, -1):
    m = max(a[2 * i + 1], a[2 * i + 2])
    need_l = m - a[2 * i + 1]
    need_r = m - a[2 * i + 2]
    #print('at', i, 'l needs', need_l, 'r needs', need_r, 'setting i to', sums[i] + a[2*i+1] + need_l)
    add += need_l + need_r
    a[i] += a[2 * i + 1] + need_l

print(add)
