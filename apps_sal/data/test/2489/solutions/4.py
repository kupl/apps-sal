N = int(input())
A = sorted(list(map(int, input().split())))
B = [0] * (A[-1] + 1)
for i in A:
    j = i
    while j <= A[-1]:
        B[j] += 1
        j += i
s = 0
for i in A:
    if B[i] == 1:
        s += 1
print(s)
