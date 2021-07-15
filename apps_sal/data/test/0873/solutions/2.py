l = int(input())
s1 = list(map(int, input().replace('', ' ').split()))
s2 = list(map(int, input().replace('', ' ').split()))
res = 0
for i in range(l):
    res += min(abs(s1[i] - s2[i]), 10 - abs(s1[i] - s2[i]))
print(res)

