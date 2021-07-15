n = int(input())
m = int(input())
a = list(map(float, input().split()))
b = list(map(float, input().split()))
if 1 in a or 1 in b:
    print(-1)
    return
payload = m
payload += payload / (a[0] - 1)
for i in range(n - 1, 0 , -1):
    payload += payload / (a[i] - 1)
    payload += payload / (b[i] - 1)
payload += payload / (b[0] - 1)
print(payload - m)

