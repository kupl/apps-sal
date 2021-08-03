n, k = list(map(int, input().split()))
s = input()
alph = "qwertyuiopasdfghjklzxcvbnm"
ti = [0] * 26
num = 1
for i in range(1, n):
    if s[i] == s[i - 1]:
        num += 1
    else:
        if num >= k:
            ti[alph.find(s[i - 1])] += num // k
        num = 1
if num >= k:
    ti[alph.find(s[-1])] += num // k
print(max(ti))
