def mp():
    return map(int, input().split())


n = int(input())
s = input()

l = -1
for i in range(n - 1):
    if s[i] > s[i + 1]:
        l = i + 1
        break
if [i for i in s] == sorted([i for i in s]):
    print('NO')
else:
    print('YES')
    print(l, l + 1)
