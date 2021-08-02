
def dev2(a):
    ans = 0
    while a % 2 == 0:
        ans += 1
        a /= 2
        if a == 0:
            break
    return ans


n = int(input())
ans = 0
ans_num = 0
for i in range(1, n + 1):
    if ans < dev2(i):
        ans_num = i
        ans = dev2(i)
print((1 if n == 1 else ans_num))
