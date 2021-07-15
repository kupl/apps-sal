s = list(input())
n = len(s)
if n % 2 == 0:
    for i in range(n//2):
        a = s[n // 2]
        if s[n // 2 - 1 - i] != a or s[n // 2 + i] != a:
            print(n // 2 + i)
            return
else:
    for i in range(1, (n - 1) // 2 + 1):
        b = s[(n-1)//2]
        if s[(n - 1) // 2 - i] != b or s[(n - 1) // 2 + i] != b:
            print((n-1)//2+i)
            return
print(n)
