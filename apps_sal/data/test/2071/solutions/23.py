n = int(input())
u1 = list(map(int, input().split()))
u2 = list(map(int, input().split()))
a1 = u1[:n]
a2 = u2[:n]
for i in range(1, n):
    a1[i] += a1[i - 1]
    a2[i] += a2[i - 1]
q1 = [0] * (2 * n)
q2 = [0] * (2 * n)
for i in range(1, n):
    q1[i] = u1[i] * (i) + q1[i - 1]
    q2[i] = u2[i] * (i) + q2[i - 1]
for i in range(n):
    q1[i + n] = u2[n - i - 1] * (n + i) + q1[i + n - 1]
    q2[i + n] = u1[n - i - 1] * (n + i) + q2[i + n - 1]
ans = q1[-1]
cur = 0
# print(ans)
for i in range(n):
    ans1 = (a1[-1] - a1[i] + a2[-1] - a2[i]) * (i + 1)
    if i % 2 == 0:
        cur += u1[i] * (i * 2)
        cur += u2[i] * (i * 2 + 1)
        ans1 += (q2[n * 2 - i - 2] - q2[i]) + cur
    else:
        cur += u2[i] * (i * 2)
        cur += u1[i] * (i * 2 + 1)
        ans1 += (q1[n * 2 - i - 2] - q1[i]) + cur
    ans = max(ans, ans1)
    #print(ans1, cur)
print(ans)
'''
3
1 100000 10000
10 100 1000
6
12 8 12 17 20 5
17 4 8 8 8 4
'''
