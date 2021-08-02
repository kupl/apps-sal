n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
s = sum(a)

res = s

while len(a) > 1:
    res += s
    s -= a.pop()

print(res)
