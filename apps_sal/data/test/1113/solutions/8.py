n = int(input())
a = list(map(int, input().split()))
s = 0

for j, i in enumerate(a):
    if i > s:
        print(j + 1)
        return
    if i == s:
        s += 1

print(-1)
