N = int(input())
S = "abcdefghijklmnopqrstuvwxyz"
ans = []
while N > 0:
    N -= 1
    ans.append(S[N % 26])
    N //= 26
print((''.join(ans[::-1])))
