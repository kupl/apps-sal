(s, k) = input().split()
k = int(k)
for i in range(0, len(s)):
    val = s[i]
    ind = i
    for j in range(i + 1, i + k + 1):
        if j < len(s) and s[j] > val:
            val = s[j]
            ind = j
    s = s[:i] + s[ind] + s[i:ind] + s[ind + 1:]
    k -= ind - i
print(s)
