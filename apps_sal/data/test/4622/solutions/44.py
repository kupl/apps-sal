N = int(input())
A = list(map(int, input().split()))
dic = {}
for num in A:
    if num not in dic:
        dic[num] = 1
    else:
        dic[num] += 1
if max(dic.values()) > 1:
    print('NO')
else:
    print('YES')
