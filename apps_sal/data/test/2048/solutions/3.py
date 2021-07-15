n = int(input())
s = list(map(int, input().split()))
c = list(map(int, input().split()))
num = float("inf")
rec1 = [float("inf")] * n
rec2 = [float("inf")] * n
for i in range(n):
    for j in range(i + 1, n):
        if s[i] < s[j] and rec1[i] > c[j]:
            rec1[i] = c[j]

for i in range(1, n):
    for j in range(i):
        if s[j] < s[i] and rec2[i] > c[j]:
            rec2[i] = c[j]

for i in range(n):
    num = min(num, rec1[i] + c[i] + rec2[i])


if num == float("inf"):
    print(-1)
else:
    print(num)
