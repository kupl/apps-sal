import sys
n, d = map(int, input().split())
count = 0
mx = 0
for i in range(d):
    s = input()
    if s == ('1' * n):
        mx = max(mx, count)
        count = 0
    else:
        count += 1
print(max(mx, count))
