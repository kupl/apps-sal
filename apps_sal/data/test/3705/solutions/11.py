n = int(input())
s = input()
k = s.count('8')
l = n - k
if k <= l // 10:
    print(k)
else:
    while k > l // 10:
        k -= 1
        l += 1
    print(min(k, l // 10))
