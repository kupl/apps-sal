n = int(input())
l = list(map(int, input().split()))
A = sum(l) - l[0]
ans = 0
for i in range(len(l)):
    ans += l[i] * A
    if A == l[-1]:
        break
    else:
        A -= l[i + 1]
print(ans % (10 ** 9 + 7))
