N = int(input())
a = [0] + list(map(int, input().split()))
b = [0 for _ in range(N + 1)]

for i in reversed(range(1, N + 1)):
    tmp = 0
    for j in range(i, N + 1, i):
        tmp += b[j]

    if(tmp % 2 == a[i]):
        b[i] = 0
    else:
        b[i] = 1


ans = []
for i, j in enumerate(b):
    if(j == 1):
        ans.append(i)
print(len(ans))
if(len(ans)):
    print(*ans)
