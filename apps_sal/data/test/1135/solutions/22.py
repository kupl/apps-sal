n = int(input())
s = input()

a = [""] * (n)

l = 1
b = 0
h = -1
for i in range(n - 1, -1, -1):
    if l % 2 == 1:
        b += 1
        a[n - b] = s[i]
    else:
        h += 1
        a[h] = s[i]
    l += 1
print("".join(map(str, a)))
