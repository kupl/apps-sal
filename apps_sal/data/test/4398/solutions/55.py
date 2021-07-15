n = int(input())
s,t = input().split()
ans = ''
for S,T in zip(s,t):
    ans += S + T

print(ans)
