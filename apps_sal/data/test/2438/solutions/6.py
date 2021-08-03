n = int(input())
s = input()
x = s[0]
l = 1
r = 0
for i in range(1, n):
    y = s[i]
    if x == y:
        r += i
        if l < i:
            r -= 1
        l += 1
    else:
        r += i - l
        l = 1
    x = y
print(r)
