# You lost the game.
n = int(input())
s = str(input())

i = 0
while i < n and s[i] =="<":
    i += 1

if i == n:
    print(n)
else:
    j = n-1
    while j >= 0 and s[j] == ">":
        j -= 1
    print(i+(n-j-1))

