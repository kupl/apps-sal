n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = int(input())
b_acc = [0]

for bi in b:
    b_acc.append(b_acc[-1] + bi)

max_length = [0] * (4 * 10**6 + 100)

for i in range(m):
    for j in range(i, m):
        B = b_acc[j + 1] - b_acc[i]
        max_length[B] = max(max_length[B], j - i + 1)

for i in range(1, 4 * 10**6 + 100):
    max_length[i] = max(max_length[i], max_length[i - 1])

a_acc = [0]

for ai in a:
    a_acc.append(a_acc[-1] + ai)

ans = 0
sb = sum(b)

for i in range(n):
    for j in range(i, n):
        A = a_acc[j + 1] - a_acc[i]
        B = x // A

        if B >= sb:
            ans = max(ans, (j - i + 1) * m)
        else:
            ans = max(ans, (j - i + 1) * max_length[B])

print(ans)
