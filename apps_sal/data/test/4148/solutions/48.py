N = int(input())
S = list(input())

for i in range(len(S)):
    uni = ord(S[i]) + N
    if uni > 90:
        uni = uni - 26
    S[i] = chr(uni)
print(''.join(S))
