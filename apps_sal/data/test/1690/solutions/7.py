n = int(input())
a = list(map(int, input().split()))
c = a[-1]
res = c
for i in a[::-1][1:]:
    if i < c:
        res += i
        c = i
    else:
        if c == 0:
            break
        res += c - 1
        c -= 1
print(res)
