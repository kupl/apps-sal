n = int(input())

dic = {chr(97 + i): 50 for i in range(26)}

for _ in range(n):
    s = list(map(str, input()))
    for key in dic:
        dic[key] = min(dic[key], s.count(key))


res = ""
for key in dic:
    if dic[key] != 0:
        res += key * dic[key]

print(res)
