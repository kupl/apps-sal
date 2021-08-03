n = int(input())
abc = "abcdefghijklmnopqrstuvwxyz"
ans = ""
while True:
    n -= 1
    ans += abc[n % 26]
    n //= 26
    if n == 0:
        print(ans[::-1])
        break
