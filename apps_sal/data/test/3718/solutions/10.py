3

def good_pair(a, b):
    return 0 < (max(a, b) - min(a, b)) <= 2

n = int(input())
balls = sorted(list(map(int, input().split())))
ans = "NO"
for i in range(n):
    a = balls[i]
    for j in range(i + 1, n):
        b = balls[j]
        for k in range(j + 1, n):
            c = balls[k]
            if good_pair(a, b) and good_pair(b, c) and good_pair(a, c):
                ans = "YES"
                break

print(ans)


