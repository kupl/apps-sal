n = int(input())
c = 1
s = ""
while n > 0:
    s += (chr(ord('a') + (n - 1) % 26))
    n = (n - 1) // 26
print(s[::-1])
