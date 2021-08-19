(n, m) = list(map(int, input().split()))
s = input()
count = {}
for val in s:
    if val not in count:
        count[val] = 0
    count[val] += 1
flag = 0
for item in count:
    if count[item] > m:
        flag = 1
        break
if flag == 0:
    print('YES')
else:
    print('NO')
