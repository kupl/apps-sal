
[n, a, b] = list(map(int, input().strip().split()))
s = input().strip() + '*'

l0 = 0
n1 = 0

i_prev = -1
while True:
    i_next = s.find('*', i_prev + 1)
    if i_next < 0:
        break
    l = i_next - i_prev - 1
    l0 += l // 2
    n1 += l % 2
    i_prev = i_next

c = min(a, b, l0)
res = 2 * c
a -= c
b -= c
l0 -= c
res += min(l0 + n1, a + b)

print(res)
