import sys
input()
k = list(map(int, input().split()))
l = []
s = [0 for i in range(200001)]
t = 1
for i in k:
    if s[i] == 1:
        s[i] = 0
    s[t] = 1
    t += 1
print(sum(s))
