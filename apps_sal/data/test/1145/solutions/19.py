n = int(input())
nums = list(map(int, input().split(' ')))
t = [0 for i in range(6002)]
ret = 0
for i in nums:
    t[i] += 1
ret = 0
for i in range(len(t)):
    if t[i] > 0:
        ret += t[i] - 1
        t[i + 1] += t[i] - 1
print(ret)
'\nInput\n4\n1 3 1 4\nOutput\n1\n\nInput\n5\n1 2 3 2 5\nOutput\n2\n'
