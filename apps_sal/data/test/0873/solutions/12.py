n = int(input())
s = [int(k) for k in input()]
s2 = [int(k) for k in input()]
t = 0
for i in range(n):
    t+=min((s[i]-s2[i])%10, (10-(s[i]-s2[i]))%10)
print(t)

