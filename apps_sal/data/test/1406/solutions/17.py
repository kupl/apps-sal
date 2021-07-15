a = input()
b = a.split()
n = int(b[0])
k = int(b[1])
d = int(b[2])
if n > k**d:
    print(-1)
    return
table = [[1]*d]
for i in range(n - 1):
    v = list(table[-1])
    j = len(v)-1
    while v[j]==k:
        v[j]=1
        j = j - 1
    v[j] = v[j] + 1
    table.append(v)
current_power = 1
answer = [0] * n
for m in range(0, d):
    current_value = 1
    for s in range(0, n):
        if s % current_power == 0 and s > 0:
            current_value = current_value % k + 1
        answer[s] = str(current_value)
    current_power *= k
    print(" ".join(answer))

