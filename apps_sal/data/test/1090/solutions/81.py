(n, k) = map(int, input().split())
s = input()
a = 'A'
cnt = 0
for i in s:
    if a != i:
        a = i
        cnt += 1
print(n - max(1, cnt - 2 * k))
