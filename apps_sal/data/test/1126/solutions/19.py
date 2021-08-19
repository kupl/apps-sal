# -*- coding: utf-8 -*-

n, x, m = map(int, input().split())

a_list = [x]
a = x
i = 1
while (i < n and i < m + 1):
    a = (a * a) % m
    a_list.append(a)
    i += 1

# print(i)
# print(a_list)

if i == n:
    ans = sum(a_list)
else:
    b = a_list.index(a)
    sum1 = sum(a_list[:b + 1])
    sum2 = sum(a_list[b + 1:i])
    blen = i - b - 1
    repeat = (n - b - 1) // blen
    amari = (n - b - 1) % blen
    sum3 = 0
    if amari != 0:
        sum3 = sum(a_list[b + 1:b + amari + 1])
    ans = sum1 + sum2 * repeat + sum3
    # print(blen)
    # print(amari)
    #print(sum1, sum2, repeat, sum3)

print(ans)
