a = int(input())
b = [int(s) for s in input().split()]
su = sum(b) - b[a - 1]
ar = b[a - 1]
ans = abs(su - ar)

for i in range(2, a - 1):
    su = su - b[a - i]
    ar = ar + b[a - i]
    tmp = abs(su - ar)
    if tmp < ans:
        ans = tmp
    tmp = 0

print(ans)
