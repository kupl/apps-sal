n, m = list(map(int, input().split()))
if m > n or m == 1 and n > 1:
    print(-1)
    return
if m == 1:
    print('a')
    return
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = ""
for i in range(2, m):
    s += l[i]

n -= (m - 2)
l = ""
l += "ab" * int(n / 2)
if (n % 2 != 0):
    l += "a"
print(l + s)
