n = int(input())
a = list(map(float, input().split()))
a.sort(reverse=True)
res = 0
l = len(a)
while a:
    res += sum(a)
    l = l // 4
    a = a[:l]
print(int(res))
