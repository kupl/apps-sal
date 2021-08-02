s = input()
t = input()
n = len(s)
m = len(t)
i = n - 1
j = m - 1
ans = 0
while(i >= 0 and j >= 0):
    if(s[i] == t[j]):
        i -= 1
        j -= 1
    else:
        ans = 1
        break

print(i + j + 2)
