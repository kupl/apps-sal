n = int(input())
a = list(map(int, input().split()))

c = [0] * 1001
for ai in a:
    c[ai] += 1
ans = 0
for t in range(max(c)):
    was = False
    for i in range(1, 1001):
        if c[i] > 0:
            if was:
                ans += 1
            else:
                was = True
            c[i] -= 1
print(ans)
            

