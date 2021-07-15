N = int(input())
s = [[0 for i in range(N)] for j in range(26)]
for i in range(N):
    t = input()
    for j in range(len(t)):
        s[ord(t[j])-ord('a')][i] += 1
ans = ''
for j in range(26):
    ans += chr(j+ord('a')) * min(s[j])
print(ans)
