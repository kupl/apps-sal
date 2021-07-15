3

def readln(): return list(map(int, input().split()))

ans = 1
l = 1
p = -1
a = input()
for i in range(len(a)):
    c = int(a[i])
    if c + p == 9:
        l += 1
    if c + p != 9 or i == len(a) - 1:
        if l % 2:
            ans *= (l + 1) // 2
        l = 1
    p = c
print(ans)

