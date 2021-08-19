N = int(input())
S = input()
ans = 0
s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(1, N):
    T1 = S[0:i]
    T2 = S[i:N]
    count = 0
    for c in s:
        if c in T1 and c in T2:
            count += 1
    ans = max(ans, count)
print(ans)
