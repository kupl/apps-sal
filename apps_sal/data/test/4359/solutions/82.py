import math
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
a = math.ceil(A * 0.1) * 10
b = math.ceil(B * 0.1) * 10
c = math.ceil(C * 0.1) * 10
d = math.ceil(D * 0.1) * 10
e = math.ceil(E * 0.1) * 10
lst1 = [A, B, C, D, E]
lst2 = [a, b, c, d, e]
last = 0
max_num = -1
for (i, j) in zip(lst1, lst2):
    if j - i > max_num:
        last = i
        max_num = j - i
ans = 0
k = lst1.index(last)
for n in range(5):
    if n == k:
        ans += lst1[n]
    else:
        ans += lst2[n]
print(ans)
