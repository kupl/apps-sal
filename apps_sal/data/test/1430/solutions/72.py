n, k = map(int, input().split())
s = input()
l = list()
s = s.replace("10", "1,0")
s = s.replace("01", "0,1")

l = [len(i) for i in s.split(",")]
r = 0
ans = 0

if s[0] == "1":
    r = min(k, len(l) - 1)
else:
    r = min(k - 1, len(l) - 1)

t = l[r]

for j in range(1, k + 1):
    # print(r,j,t,l[r-j],l[r+j])
    if r - j >= 0:
        #print("r-j >= 0:")
        t += l[r - j]
    if r + j < len(l):
        #print("r+j < len(l):")
        t += l[r + j]
ans = t
for i in range(r + 2, len(l), 2):
    for j in range(1, 3):
        if i - j - k >= 0:
            #print("l[i-j-k]", i-j-k, l[i-j-k])
            t -= l[i - j - k]
        if i + j + k - 2 < len(l):
            #print("l[i+k+j]", i+j+k-2, l[i+j+k-2])
            t += l[i + j + k - 2]
    ans = max(ans, t)
print(ans)
