f = 'ACTG'
n = int(input())
s = input()
ans = n * 26
for i in range(n - 3):
    s1 = s[i:i+4]
    cnt = 0
    for i in range(4):
        cnt += min(min(abs(ord(f[i]) - ord(s1[i])), ord('Z') - ord(s1[i]) + 1 + ord(f[i]) - ord('A')), ord(s1[i]) - ord('A') + 1 + ord('Z') - ord(f[i]))
    ans = min(ans, cnt)
print(ans)
