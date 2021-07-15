s = input()
s = s[::-1]

L = [0]
cnt = 1
for i in range(len(s)):
    L.append((L[-1]+(int(s[i])*cnt))%2019)
    cnt *= 10
    cnt %= 2019

D = dict()
for j in L:
    if j in D:
        D[j] += 1
    else:
        D[j] = 1
ans = 0
for k in D.values():
    ans += k * (k-1) //2

print(ans)
