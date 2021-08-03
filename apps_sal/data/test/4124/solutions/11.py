s = str(input())
n = len(s)
t = str(input())
m = len(t)
k = 0
while n - k - 1 >= 0 and m - k - 1 >= 0 and s[n - k - 1] == t[m - k - 1]:
    k += 1
print(n + m - 2 * k)
