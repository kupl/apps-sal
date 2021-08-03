n = int(input())
seq = list(map(int, input().split()))

money = [0 for i in range(101)]

for i in seq:
    if i == 50:
        if money[25] >= 1:
            money[25] -= 1
        else:
            print("NO")
            return
    elif i == 100:
        if money[50] >= 1 and money[25] >= 1:
            money[50] -= 1
            money[25] -= 1
        elif money[25] >= 3:
            money[25] -= 3
        else:
            print("NO")
            return

    money[i] += 1

print("YES")
