n = int(input())
aa = [
    list(map(int, input().split()))
    for _ in range(2)
]

if n == 1:
    print(aa[0][0] + aa[1][0])
    return

for i in range(1, n):
    aa[1][-i - 1] += aa[1][-i]
for i in range(1, n):
    aa[0][-i - 1] += max(aa[1][-i - 1], aa[0][-i])
print(aa[0][0])
