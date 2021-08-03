n = int(input())

money = [1]
for i in range(1, 7):
    money.append(6**i)
for i in range(1, 6):
    money.append(9**i)
money = sorted(money)

lst = [0] * 1000000
for i in range(n + 1):
    can = i
    for m in money:
        if i - m >= 0:
            can = min(can, lst[i - m] + 1)
        else:
            break
    lst[i] = can

print(lst[n])
