p = int(input())
ans = 0


def solve(p):
    cnt = 0
    for i in range(1, p + 1):
        if p % i == 0:
            cnt += 1
    if cnt == 8 and p % 2 == 1:
        return True
    return False


for i in range(1, p + 1):
    if solve(i) == True:
        ans += 1

print(ans)
