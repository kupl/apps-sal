n = input()
n = int(n)
a = input()
a = a.split()
a = [int(i) for i in a]
num = []
for _ in range(n):
    num.append(list())
for _, i in enumerate(a):
    num[i-1].append(_)
answer = num[0][0] + num[0][1]
for n in range(len(num)-1):
    answer = answer + min(abs(num[n][0] - num[n+1][0]) + abs(num[n][1] - num[n+1][1]),
                          abs(num[n][0] - num[n+1][1]) + abs(num[n][1] - num[n+1][0]))
print(answer)
