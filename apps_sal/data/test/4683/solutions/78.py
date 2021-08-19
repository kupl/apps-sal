n = int(input())
li = list(map(int, input().split()))
s = sum(li)
c = 0
for i in range(n - 1):
    s -= li[i]
    c += li[i] * s
print(c % (10 ** 9 + 7))
