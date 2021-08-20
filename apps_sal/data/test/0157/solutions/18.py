a = int(input())
b = int(input())
c = int(input())
ans = 0
while a > 0 and b > 1 and (c > 3):
    a -= 1
    b -= 2
    c -= 4
    ans += 7
print(ans)
