s = input()
mod = 2019
dic = [0] * mod
dic[0] += 1

tmp = 0
d = 1
for i in reversed(range(len(s))):
    tmp += int(s[i]) * d
    tmp %= mod
    d *= 10
    d %= mod
    dic[tmp] += 1

ans = [i * (i-1) / 2 for i in dic]
print(int(sum(ans)))
