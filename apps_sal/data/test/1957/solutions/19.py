(n, A, B) = list(map(int, input().split()))
otv = list(map(int, input().split()))
one = otv.pop(0)
otv.sort()
su = sum(otv) + one
res = 0
while B * su > A * one:
    res += 1
    su -= otv.pop()
print(res)
