n = int(input())
L = [int(i) for i in input().split()]
s = 0
for i in range(len(L)):
    s = s + L[i] * i * 4
print(s)
