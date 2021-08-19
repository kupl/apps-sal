n = int(input())
s = input()
div = 1
while div <= n:
    if n % div == 0:
        tmp = s[:div]
        s = tmp[::-1] + s[div:]
    div += 1
print(s)
