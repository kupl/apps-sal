n, m = map(int, input().split())
x = [int(x1) for x1 in input().split()]

pre1 = [0] * (n + 2)
pre2 = [0] * (n + 1)
pre3 = [0] * (n + 1)

for i in range(0, len(x) - 1):
    a = min(x[i], x[i + 1])
    b = max(x[i], x[i + 1])

    if(b - a > 1):

        pre1[a + 1] += 1
        pre1[b] += -1

    if(a != b):
        pre2[a] += (b - 1) - (b - a)  # (b-a-1)+b
        pre3[b] += a - (b - a)


t = 0
for i in range(0, len(pre1)):
    pre1[i] = t + pre1[i]
    t = pre1[i]

# print('pre1',pre1)
# print('pre2',pre2)
# print('pre3',pre3)


ans = 0
for i in range(0, m - 1):
    ans += abs(x[i] - x[i + 1])


print(ans, end=" ")
for i in range(2, n + 1):
    temp = ans + pre2[i] + pre3[i] + -pre1[i]
    print(temp, end=" ")

print(" ")
