s = str(input())
k = int(input())
l = [0 for i in range(26)]
a = 0
if k > len(s):
    print("impossible")
    return
for c in s:
    if l[ord(c) - 97] == 0:
        l[ord(c) - 97] = 1
        a += 1
if a <= k:
    print(k - a)
else:
    print(0)
