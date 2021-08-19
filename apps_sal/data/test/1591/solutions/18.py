(n, k) = map(int, input().split())
a = []
s = set()
ans = 0
k = 0
for i in range(n):
    a = int(input())
    if a in s:
        s.remove(a)
        ans += 2
        k += 1
    else:
        s.add(a)
print(ans + (n // 2 + n % 2) - k)
