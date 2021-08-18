
def S(n):
    if n < 10:
        return n
    return S(n // 10) + n % 10


li = []

for d in range(20):
    a = 10**d
    for x in range(200):
        y = (x + 1) * a - 1
        if y > 0:
            z = S(y)
            li.append((y, z))

li = sorted(list(set(li)), reverse=True)

answer = []
min_N, min_S = li[0]
for n, s in li[1:]:
    if n * min_S <= s * min_N:
        min_N = n
        min_S = s
        answer.append(n)


K = int(input())
answer.sort()
answer = answer[:K]
print(('\n'.join(map(str, answer))))
