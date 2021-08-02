n = int(input())
s = input()
res = n
e = s.count("E")

l_w = 0
l_e = 0
for i in range(n):
    if i == n - 1 and s[i] == "E":
        l_e += 1
    tmp = l_w + (e - l_e)
    res = min(tmp, res)
    if s[i] == "W":
        l_w += 1
    else:
        l_e += 1
print(res)
