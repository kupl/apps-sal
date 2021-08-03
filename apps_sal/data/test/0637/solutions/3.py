n = int(input())
line = list(map(int, input().split()))
ans = [1]
prev = line[0]
k = 1
for i in range(1, n):
    if line[i] == prev:
        ans[-1] += 1
    else:
        k += 1
        prev = line[i]
        ans.append(1)
if [ans[0]] * k != ans:
    print('NO')
else:
    print('YES')
