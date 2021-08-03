import random

mod = 998244353
N, X = input().split()
N = int(N)
A = []
for i in range(N):
    A.append(int(input(), 2))
A.sort()

a = A[-1]
M = max(len(X) - 1, a.bit_length() - 1)
data = [0] * (M + 1)
n = a.bit_length() - 1
for i in range(M - n, -1, -1):
    data[i + n] = a << i

for i in range(0, N - 1):
    a = A[i]
    flag = True
    while flag:
        n = a.bit_length()
        for j in range(n - 1, -1, -1):
            a = min(a, a ^ data[j])
        if a != 0:
            data[a.bit_length() - 1] = a
            id = a.bit_length() - 1
            while data[id + 1] == 0:
                data[id + 1] = min((data[id] << 1) ^ a, (data[id] << 1))
                if data[id + 1]:
                    id += 1
                else:
                    flag = False
            else:
                a = data[id] << 1
        else:
            break

data2 = [0] * (M + 1)
for i in range(M + 1):
    data2[i] = (data[i] != 0)

for i in range(1, M + 1):
    data2[i] += data2[i - 1]

data2 = [0] + data2

# print(data)
# print(data2)

x = 0
ans = 0
n = len(X) - 1
for i in range(len(X)):
    if X[i] == "1":
        if x >> (n - i) & 1 == 1:
            if data[n - i]:
                ans += pow(2, data2[n - i], mod)
                ans %= mod
        else:
            ans += pow(2, data2[n - i], mod)
            ans %= mod
            if data[n - i]:
                x = x ^ data[n - i]
            else:
                break
    else:
        if x >> (n - i) & 1 == 1:
            if data[n - i]:
                x = x ^ data[n - i]
            else:
                break
        else:
            continue
else:
    ans += 1
    ans %= mod
print(ans)
