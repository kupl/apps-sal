N = int(input())
A = list(map(int, input().split()))
li = [0] * (N + 1)
total = 0
for i in A:
    li[i] += 1
for i in li[1:]:
    total += i * (i - 1) // 2
for i in A:
    j = li[i]
    print(total - j * (j - 1) // 2 + (j - 1) * (j - 2) // 2)
