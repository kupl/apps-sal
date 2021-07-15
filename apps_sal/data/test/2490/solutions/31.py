n = input().rstrip()

total = 0
carry = 0
for i in range(len(n)-1, -1, -1):
    v = int(n[i]) + carry
    if v > 5:
        total += 10 - v
        carry = 1
    elif v == 5:
        if i == 0:
            total += 5
            carry = 0
        else:
            if int(n[i-1]) >= 5:
                total += 5
                carry = 1
            else:
                total += 5
                carry = 0
    else:
        total += v
        carry = 0

print(total + carry)
