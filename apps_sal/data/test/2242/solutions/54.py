S = list(input())
S = list(map(int, S))[::-1]
mod = [0] * 2019
mod[0] += 1
ans = 0
temp = 0
p = 1
for i in range(len(S)):
    temp += S[i] * p
    p = p * 10 % 2019
    temp %= 2019
    ans += mod[temp]
    mod[temp] += 1
print(ans)
