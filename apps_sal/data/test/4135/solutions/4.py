n = int(input())
s = input()
for x in range(1, n + 1):
    if(n % x == 0):
        s = s[:x][::-1] + s[x:]
print(s)
