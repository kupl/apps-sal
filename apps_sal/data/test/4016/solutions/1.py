n, k = map(int, input().split())
t = input()

double = 0
for i in range(1, n):
    if t[-i:] == t[:i]:
        double = i

print(t + t[double:] * (k - 1))
