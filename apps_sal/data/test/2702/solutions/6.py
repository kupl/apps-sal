n = int(input())
data = []
for _ in range(n):
    temp = list(input().split())
    val = ''
    for i in temp:
        if(i == 'T'):
            val += '1'
        else:
            val += '0'
    data.append(int(val, 2))
f = {}
for i in data:
    if(i in f):
        f[i] += 1
    else:
        f[i] = 1
ans = [0]

for i in data:
    if(bin(i).count('1') == f[i]):
        ans.append(f[i])

print(max(ans))
