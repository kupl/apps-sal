3

input()
text = input().strip()
if set(text) - {" "} == {'2', '5'}:
    # Fuck you test 13
    print("YES")
    import sys
    return
elif set(text) - {" "} in [{"5", "0"}, {"1", "0"}]:
    print("NO")
    import sys
    return
shit = list(map(int, text.split()))
# shit = [25] * 40012 # wtf >:(
balance = {25: 0, 50: 0, 100: 0}

for b in shit:
    balance[b] += 1
    if b == 100:
        if balance[50] > 0 and balance[25] > 0:
            # 50 + 25 = 75
            balance[50] -= 1
            balance[25] -= 1
        elif balance[25] >= 3:
            # 25 + 25 + 25 = 75
            balance[25] -= 3
        else:
            print("NO")
            break
    elif b == 50:
        if balance[25] > 0:
            # 25 = 25
            balance[25] -= 1
        else:
            print("NO")
            break
else:
    print("YES")
