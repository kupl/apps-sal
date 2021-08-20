s = list(input())
n = len(s)
m = int(input())
ai = list(map(int, input().split()))
ai.sort()
z = 0
for i in range(m):
    if i % 2 != 0:
        temp = n - ai[i]
        temp2 = n - z
        temp3 = reversed(s[z:ai[i] - 1])
        s[z:ai[i] - 1] = reversed(s[temp + 1:temp2])
        s[temp + 1:temp2] = temp3
    z = ai[i] - 1
if m % 2 != 0:
    s[ai[-1] - 1:n - ai[-1] + 1] = reversed(s[ai[-1] - 1:n - ai[-1] + 1])
print(''.join(s))
