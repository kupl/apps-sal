n = int(input())
a = list(map(int, input().split()))
p = a[0]
a = [(p, 0)] + sorted([(a[i], i) for i in range(1, n)], reverse=True)
result = ''
got = {0}
for i in range(n):
    temp_a = a[i][0]
    temp_i = i + 1
    while temp_a > 0 and temp_i < n:
        if temp_i not in got:
            got.add(temp_i)
            temp_a -= 1
            result += str(a[i][1] + 1) + ' ' + str(a[temp_i][1] + 1) + '\n'
        temp_i += 1
if len(got) < n:
    print(-1)
else:
    print(n - 1)
    print(result)
