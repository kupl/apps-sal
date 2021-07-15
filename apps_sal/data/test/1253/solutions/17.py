n, k = map(int, input().split())
l = list(map(int, input().split()))
l.sort(key=abs, reverse=True)
result = 0
for i in l:
    if k > 0 and i < 0:
        result -= i
        k -= 1
    else:
        result += i
if k % 2 == 1:
    result -= 2 * abs(l[-1])
print(result)
