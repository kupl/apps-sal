import math
N, A, B = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
dic = {}
for i in range(N):
    v = a[i]
    if v not in dic.keys():
        dic[v] = 1
    else:
        dic[v] += 1
tmp = 0
num_used = {}
m = 10**18
M = -1
for i in range(A):
    v = a[i]
    m = min(m, v)
    M = max(M, v)
    tmp += v
    if v not in num_used.keys():
        num_used[v] = 1
    else:
        num_used[v] += 1
max_ave = tmp / A
print(max_ave)
if num_used[m] == dic[m]:
    print(1)
elif m == M:
    x = dic[m]
    y = num_used[m]
    cnt = 0
    for i in range(y, min(x + 1, B - A + y + 1)):
        cnt += math.factorial(x) // math.factorial(i) // math.factorial(x - i)
    print(cnt)
else:
    x = dic[m]
    y = num_used[m]
    cnt = math.factorial(x) // math.factorial(y) // math.factorial(x - y)
    print(cnt)
