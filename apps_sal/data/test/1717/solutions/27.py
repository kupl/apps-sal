def gcm(a, b):
    if b % a == 0:
        return a
    return gcm(b % a, a)


def gcm_2(a, b):
    Gcm = gcm(a, b)
    return a * b / Gcm


N = int(input())

ans = 2
for i in range(3, N + 1):
    ans = gcm_2(ans, i)
ans += 1
print(int(ans))
