n = int(input())
a = list(map(int, input().split()))
curr = 1
while curr < n and a[curr] > a[curr - 1]:
    curr += 1
while curr < n and a[curr] == a[curr - 1]:
    curr += 1
while curr < n and a[curr] < a[curr - 1]:
    curr += 1
if curr == n:
    print('YES')
else:
    print('NO')
