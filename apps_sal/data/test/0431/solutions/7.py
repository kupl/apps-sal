def booly(s):
    return bool(int(s))


n, m = list(map(int, input().split()))

nothing = "0" * (m + 2)

a = []
for i in range(n):
    a.append(input())

for i in range(n):
    if a[i] != nothing:
        break

a = a[i:]
a.reverse()

n = len(a)

# print(a)

leftA = [i.find("1") for i in a]
rightA = [i.rfind("1") for i in a]

for i in range(n):
    if leftA[i] == -1:
        leftA[i] = m + 1
    if rightA[i] == -1:
        rightA[i] = 0

#print(leftA, rightA);

if len(a) == 1:
    print(rightA[0])
    return

left = [None] * (n + 1)
right = [None] * (n + 1)

left[0] = rightA[0] * 2
right[0] = m + 1

for i in range(1, n - 1):
    left[i] = 1 + min(left[i - 1] + rightA[i] * 2, right[i - 1] + m + 1)
    right[i] = 1 + min(right[i - 1] + (m + 2 - 1 - leftA[i]) * 2, left[i - 1] + m + 1)

#print(left, right)

print((min(1
           + left[n-2]
           + rightA [n - 1],
           1 + right[n - 2]
           +  (m+2 - 1 - leftA[n-1]))));
