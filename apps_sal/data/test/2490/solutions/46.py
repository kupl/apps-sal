N = list(map(int, input()))
ans = 0
carry = 0
for i in range(len(N) - 1, -1, -1):
    if carry == 2:
        if N[i] >= 5:
            digit = N[i] + 1
            carry = 1
            ans += 10 - digit
        else:
            digit = N[i]
            carry = 0
            ans += digit
    else:
        digit = N[i] + carry
        if digit >= 6:
            carry = 1
            ans += 10 - digit
        elif digit <= 4:
            carry = 0
            ans += digit
        else:
            carry = 2
            ans += digit
if carry == 1:
    ans += carry
print(ans)
