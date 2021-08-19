N = int(input())
S = input()
ans = ''
Z_s = 'Z'
for i in range(len(S)):
    ord_s = ord(S[i]) + N
    if ord_s > ord(Z_s):
        ord_s -= ord('Z') - ord('A') + 1
    ans += chr(ord_s)
print(ans)
