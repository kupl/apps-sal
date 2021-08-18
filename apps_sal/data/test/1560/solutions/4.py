n = int(input())
s = input()

cwred = 0
cwblack = 0

res = 0

for i in range(n):
    if i % 2 == 0 and s[i] == 'b':
        cwblack += 1
    if i % 2 == 1 and s[i] == 'r':
        cwred += 1

res = min(cwblack, cwred) + abs(cwblack - cwred)

cwred = 0
cwblack = 0

for i in range(n):
    if i % 2 == 1 and s[i] == 'b':
        cwblack += 1
    if i % 2 == 0 and s[i] == 'r':
        cwred += 1

if res > min(cwblack, cwred) + abs(cwblack - cwred):
    res = min(cwblack, cwred) + abs(cwblack - cwred)

print(res)
