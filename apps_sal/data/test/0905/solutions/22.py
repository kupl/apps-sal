n, s = input().split()
ans = -1
s = int(s)
for i in range(0, int(n)):
    a, b = input().split()
    a = int(a)
    b = int(b)
    if(s > a or (s == a and b == 0)):
        ans = max(ans, (100 - b) % 100)

print(ans)
