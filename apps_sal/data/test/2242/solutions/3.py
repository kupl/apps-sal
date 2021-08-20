S = input()
N = len(S)
q = [0]
count = [0 for i in range(2019)]
ans = 0
count[0] = 1
m10 = 1
for i in range(1, N + 1):
    a = int(S[-i])
    q.append((a * m10 + q[i - 1]) % 2019)
    m10 *= 10
    m10 %= 2019
    count[q[-1]] += 1
for i in range(2019):
    c = count[i]
    ans += c * (c - 1) // 2
print(ans)
