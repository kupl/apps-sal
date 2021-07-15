n = int(input())
d = int(input())
e = int(input())

e = 5*e

curr = 0
mini = n

while curr <= n:
    if (n-curr)%e < mini:
        mini = (n-curr)%e
    curr += d

print(mini)
