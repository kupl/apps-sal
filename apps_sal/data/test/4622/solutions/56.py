N = int(input())
A = list(map(int, input().split()))
dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
M = max(dic.values())
print('YES' if M == 1 else 'NO')
