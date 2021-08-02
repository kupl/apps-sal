n = int(input())
a = list(map(int, input().split()))

num = [0] * (10**6 + 1)

for x in a:
    num[x] += 1

f = 1
for i in range(2, 10**6 + 1):
    s = sum(num[i::i])
    if s == n:
        print("not coprime")
        return
    if s > 1:
        f = 0
if f == 0:
    print("setwise coprime")
else:
    print("pairwise coprime")
