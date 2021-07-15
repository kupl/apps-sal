n = int(input())
dic = {}

A = list(map(int, input().split()))

for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

ans = 0

for key in dic:
    if dic[key] != key:
        if dic[key] > key:
            ans += dic[key] - key
        else:
            ans += dic[key]

print(ans)
