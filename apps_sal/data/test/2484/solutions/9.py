n = int(input())
a = list(map(int, input().split()))

s = [0] * n
t = [0] * n

s[0] = a[0]
t[0] = a[0]

for i in range(1, n):
    s[i] = s[i-1] + a[i]
    t[i] = t[i-1] ^ a[i]

s = [0] + s
t = [0] + t 

ans = 0
#print(s, t)

l = 1
r = l
while l < n+1:
    #print(l, r)
    if s[r] - s[l-1] == t[r] ^ t[l-1]:
        while True:
            #print(l, r, s[r] - s[l-1], t[r] ^ t[l-1])
            if s[r] - s[l-1] == t[r] ^ t[l-1]:
                r += 1
                if r > n:
                    ans += r - l
                    r = n
                    break
            else:
                ans += r - l 
                break
    else:
        while True:
            #print(l, r, s[r] - s[l-1], t[r] ^ t[l-1])
            if s[r] - s[l-1] == t[r] ^ t[l-1]:
                ans += r - l + 1
                break
            else:
                r -= 1
                if r == l:
                    ans += 1
                    r = l + 1
                    break

    l += 1

print(ans)
