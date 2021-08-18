n = int(input())
s = input()
c = '&'
ans = ""

i = 0
while (i < n):
    j = i
    while (j + 1 < n and s[j + 1] == s[i]):
        j += 1

    if i == j - 1 and (s[i] == 'e' or s[i] == 'o'):
        ans += s[i]
        ans += s[i + 1]
    elif (s[i] == 'e' or s[i] == 'a' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'y'):
        ans += s[i]
    else:
        k = i
        while (k <= j):
            ans += s[k]
            k += 1

    i = j + 1

print(ans)
