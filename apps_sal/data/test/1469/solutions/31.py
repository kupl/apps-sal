
L = int(input())

digit = L.bit_length()  # 必要なビット数(頂点数)

if 2**digit > L :
    digit -= 1

ans = []
for i in range(1, digit+1) :
    ans.append([i, i+1, 0])
    ans.append([i, i+1, 2**(i-1)])

L = L - 2**digit  # 残り本数

tmp = 0
for i in range(digit, 0, -1) :
    if L - 2**(i - 1) >= 0 :
        ans.append([i, digit+1, 2**digit + tmp])
        L -= 2**(i - 1)
        tmp += 2**(i - 1)

print(digit+1, len(ans))
for a in ans :
    print(*a)
