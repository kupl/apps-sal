n = int(input())
states = input().split()
op = 0
carry = 0
for i in range(0, n):
    if states[i] == '1':
        op = op + 1 + carry
        carry = 0
        if i + 1 < n:
            if states[i + 1] == '1':
                continue
            else:
                carry = 1
print(op)
