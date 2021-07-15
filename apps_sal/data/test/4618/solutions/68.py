s = input()
l = len(s)
k = int(input())
A = set()
for i in range(l):
    for j in range(1, 6):
        if i+j <= l:
            A.add(s[i:i+j])
ANS = sorted(A)
print((ANS[k-1]))

