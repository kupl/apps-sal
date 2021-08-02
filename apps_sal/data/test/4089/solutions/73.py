n = int(input())
abc = "abcdefghijklmnopqrstuvwxyz"
ans = ""

while True:
    n -= 1
    m = n % 26
    ans += abc[m]
    n = n // 26
    if n == 0:
        break

print((ans[::-1]))
