N = int(input())
s = list(map(int, input().split()))
s_max = max(s)
s_min = min(s)
A = []
for i in range(s_min, s_max + 1):
    b = 0
    for j in s:
        b += (j - i) ** 2
    A.append(b)
print(min(A))
