n = int(input())
s = input()
for i in range(2, n + 1):
    if(n % i == 0):
        t = s[:i]
        t = t[::-1]
        tt = s[i:]
        s = t + tt
print(s)
