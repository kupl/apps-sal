n = int(input())
s = input()

for i in range(2, n + 1):
    if(n % i == 0):
        d = ""
        for j in range(i - 1, -1, -1):
            d = d + s[j]
        d += s[i:]
        s = d
print(s)
