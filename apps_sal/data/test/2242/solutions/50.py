S = input()
N = len(S)
 
counter = [0] * 2019
counter[0] = 1
T = 0
R = 1
for i in range(N):
    T = (T + R * int(S[N - i - 1])) % 2019
    R = 10 * R % 2019
    counter[T] += 1
 
ans = 0
for i in range(2019):
    m = counter[i]
    ans += m * (m - 1) // 2
 
print(ans)
