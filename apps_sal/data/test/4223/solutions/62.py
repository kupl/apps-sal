n = int(input())
s = [i for i in input()]
result  = []
tmp = '¥'
for i in range(0,n):
    if tmp != s[i]:
        result.append(s[i])
        tmp = s[i]
print(len(result))
