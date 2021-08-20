n = int(input())
a = list(map(int, input().split()))
ans = 1000000000.0
for p in range(-100, 101):
    sub = 0
    for q in a:
        sub += pow(p - q, 2)
    ans = min(ans, sub)
print(ans)
