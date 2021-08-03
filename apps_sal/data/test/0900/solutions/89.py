s = input()
pre = [1] + [0] * 12
n = 10**9 + 7
tem = [[i * j % 13 for i in range(10)] for j in range(13)]
t = 1
for i in range(len(s)):
    if s[-1 * i - 1] > "9":
        pre = [sum([pre[k - i] for i in tem[t]]) % n for k in range(13)]
    else:
        te = int(s[-1 * i - 1]) * t % 13
        pre = [pre[i - te] for i in range(13)]
    t = t * 10 % 13
print(pre[5])
