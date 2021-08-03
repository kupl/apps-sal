n = int(input())
c = 0
while 1:
    c += 1
    if n == 0:
        break
    if n > 0:
        if c % 2 == 1:
            if (4**(c // 2 + 1) - 1) // 3 >= n:
                break
    elif n < 0:
        if c % 2 == 0:
            if abs(2 * (4**(c // 2) - 1)) // 3 >= abs(n):
                break
if n == 0:
    ans = ["0"]
else:
    k = 0
    ans = []
    while k < c:
        ans.append(str(n % 2))
        n = (-1) * (n // 2)
        k += 1
print("".join(ans[::-1]))
