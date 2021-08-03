def nt(t):
    t = t % (60 * 24)
    return '7' in str(t // 60) + str(t % 60)


x = int(input())
h, m = [int(i) for i in input().split()]
t = h * 60 + m
ans = 0
while not nt(t):
    t = (t - x) % (60 * 24)
    ans += 1
print(ans)
