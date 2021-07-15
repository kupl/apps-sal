#!/usr/bin/env python3
import math

n = int(input())

mod = 10**9+7

data = {}
zero_zero = 0

for i in range(n):
    a, b = list(map(int, input().split()))
    # # print(a, b)
    if a == 0 and b == 0:
        zero_zero += 1
        continue
    gcd = math.gcd(a, b)
    a, b = a//gcd, b//gcd
    if a < 0:
        a, b = -a, -b

    if a == 0:  # (0, 1)
        a, b = 0, 1

    elif b == 0:  # (1, 0)
        a, b = 1, 0

    # print(a, b)
    # print()

    if b <= 0:  # (+, -) or (1, 0)
        if (-b, a) in data:
            data[(-b, a)][1] += 1
        else:
            data[(-b, a)] = [0, 1]
    elif b > 0:  # (+, +) or (1, 0)
        if (a, b) in data:
            data[(a, b)][0] += 1
        else:
            data[(a, b)] = [1, 0]

# print(data)
# print(zero_zero)

power_2 = [1]
for i in range(1, 2*10**5+100):
    power_2.append(power_2[i-1]*2 % mod)

ans = 1
# print(ans)
# print()
for (a, b), (l, m) in list(data.items()):
    ans *= (power_2[l]+power_2[m]-1) % mod
    # print(power_2[l]+power_2[m]-1)
    # print(ans)
    # print()

ans = ans - 1  # removed not selected
ans += zero_zero
print((ans % mod))
# count_pp = 0
# count_pm = 0
# ans = 0
# while(1):
#     pp_tmp = plus_plus[count_pp]
#     pm_tmp = plus_minus[count_pm]

#     print("pp_tmp", pp_tmp)
#     print("pm_tmp", pm_tmp)

#     if pp_tmp[0]*pm_tmp[0] + pp_tmp[1]*pm_tmp[1] == 0:
#         pp_mag, pm_mag = 1, 1  # magnitude
#         while(1):
#             if count_pp < len(plus_plus)-1:
#                 if plus_plus[count_pp] == plus_plus[count_pp+1]:
#                     pp_mag += 1
#                     count_pp += 1
#                 else:
#                     break
#             else:
#                 break
#         while(1):
#             if count_pm < len(plus_minus)-1:
#                 if plus_minus[count_pm] == plus_minus[count_pm+1]:
#                     pm_mag += 1
#                     count_pm += 1
#                 else:
#                     break
#             else:
#                 break
#         ans += pp_mag*pm_mag

#     elif pp_tmp[2]*pm_tmp[2] > -1:
#         count_pp += 1

#     elif pp_tmp[2]*pm_tmp[2] < -1:
#         count_pm += 1

#     if count_pp == len(plus_plus)-1:
#         break
#     if count_pm == len(plus_minus)-1:
#         break
#     print(1)

# ans += zero_zero
# n = n - zero_zero
# count = ((n % mod) * ((n-1) % mod))//2
# count -= (negative) % mod

# print(count % mod)

