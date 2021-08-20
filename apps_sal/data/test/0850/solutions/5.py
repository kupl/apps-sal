def check(a, b):
    while a and b:
        if a % 10 and b % 10:
            return False
        a //= 10
        b //= 10
    return True


K = int(input())
d = sorted(map(int, input().split()))
flag = False
if d and (not d[0]):
    flag = True
    del d[0]
ans = [d[0]] if d else []
for i in range(len(d)):
    for j in range(i):
        if check(d[i], d[j]):
            for k in range(j):
                if check(d[i], d[k]) and check(d[j], d[k]):
                    ans = [d[i], d[j], d[k]]
            if len(ans) < 2:
                ans = [d[i], d[j]]
if flag:
    ans.append(0)
print(len(ans))
print(*ans)
