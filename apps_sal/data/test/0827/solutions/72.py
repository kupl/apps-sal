import sys
N = int(input())
T = input()

if T == "0":
    print(10 ** 10)
    return
elif T == "1":
    print(2 * 10 ** 10)
    return
elif T == "11" or T == "10":
    print(10 ** 10)
    return
elif T == "01":
    print(10 ** 10 - 1)
    return

if T[0] == "0":
    T = "11" + T
elif T[0] == "1" and T[1] == "0":
    T = "1" + T

for i in range(len(T)):
    if i % 3 == 2 and T[i] != "0":
        print(0)
        return
    elif i % 3 != 2 and T[i] != "1":
        print(0)
        return

T_amnt = len(T)
T_sho = T_amnt // 3
T_amari = T_amnt % 3

if T_amari == 0:
    amari = 1
else:
    amari = 0
print(10**10 - T_sho + amari)
