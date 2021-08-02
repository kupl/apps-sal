def ok(x, k, s, n):
    i = 0
    k -= 1
    while i < len(s):
        if(i + x + 1 >= len(s)):
            k -= 1
            #print(len(s) - 1)
            break
        j = n[i + x + 1]
        if(j == i):
            return 0
        i = j

        # print(i)
        k -= 1
        if i == len(s) - 1:
            break
    # print(k)
    return k >= 0


n, k = list(map(int, input().split()))
s = input()
n = [0]
for i in range(1, len(s)):
    if s[i] == '0':
        n.append(i)
    else:
        n.append(n[-1])
#print(ok(2, k, s, n))
# return
l = -1
r = len(s)
while r - l > 1:
    m = (l + r) // 2
    if ok(m, k, s, n):
        r = m
    else:
        l = m
print(r)
