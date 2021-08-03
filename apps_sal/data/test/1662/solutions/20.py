n = int(input())
s = sorted(map(int, input().split()))
m = 5001
c = [0] * m
for i in range(n):
    c[s[i]] += 1
c[s[-1]] = 1
a = [i for i in range(m) if c[i] > 0] + [i for i in range(m) if c[i] > 1][::-1]
print(len(a))
print(' '.join(map(str, a)))
