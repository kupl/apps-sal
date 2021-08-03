n = input()
a_in = list(map(int, input().split()))
a = list(reversed(sorted(a_in)))
prev = 1000000001
ans = 0
for c in a:
    if c >= prev:
        c = prev - 1
    if c <= 0:
        break
    ans += c
    prev = c
print(ans)
