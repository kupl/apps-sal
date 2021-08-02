rubes = int(input())
d = int(input())
e = int(input()) * 5

ans = rubes
for i in range(rubes // e + 1):
    ans = min(ans, (rubes - i * e) % d)
print(ans)
