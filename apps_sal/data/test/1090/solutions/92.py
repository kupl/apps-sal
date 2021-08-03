n, k = list(map(int, input().split()))
s = input()

rl = s.count('RL')
if s[0] == 'L':
    start = 1
else:
    start = 0
if s[-1] == 'R':
    end = 1
else:
    end = 0
a = rl - k
if a >= 1:
    ans = a * 2 + start + end
elif a == 0:
    ans = start + end
elif a <= -1:
    ans = 1
print((n - ans))
