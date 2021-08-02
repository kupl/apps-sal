def vten(c, n):
    c = str(c)
    ans = 0
    for i in range(0, len(c)):
        ans += int(c[len(c) - i - 1]) * n ** i
    return ans


def vk(ch, k):
    ans = ''
    while ch != 0:
        ans += str(ch % k)
        ch //= k
    return ans[::-1]


ans = []
for x in range(60):
    for i in range(1, x + 1):
        s = '1' * i
        s += '0'
        s += '1' * (x - i)
        y = vten(int(s), 2)
        ans.append(y)

a, b = list(map(int, input().split()))
answer = 0
for i in ans:
    if i >= a and i <= b:
        answer += 1
print(answer)
