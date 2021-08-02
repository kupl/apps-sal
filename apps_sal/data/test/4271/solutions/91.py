n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
su = 0
n1 = len(a)
for i in a:
    su += b[i - 1]

for i in range(n1 - 1):
    if a[i] == a[i + 1] - 1:
        su += c[a[i] - 1]

print(su)
