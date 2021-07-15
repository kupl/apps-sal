n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = 0
j = 0
ans = 0
s = set()
while i < len(a):
    if a[i] in s:
        i += 1
        continue
    while b[j] != a[i]:
        s.add(b[j])
        ans += 1
        j += 1
    i += 1
    j += 1
print(ans)

