n = int(input())
n1 = 1
n2 = 1
temp = n2
s = ["o"]*n
s[0] = "O"
while n >= n2:
    s[n2-1] = "O"
    temp = n2
    n2 = n1 + n2
    n1 = temp
for i in range(n):
    print(s[i],end="")

