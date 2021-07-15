s = input().split()
n = int(s[0])
m = int(s[1])
p = 101
for i in range(n):
    s = input().split()
    x = int(s[0])/int(s[1])
    if x<p:
        p=x

print(m*p)
