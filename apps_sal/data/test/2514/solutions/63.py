n = int(input())
a = [int(x) for x in input().split()]
q = int(input())
s = [0] * (10**5 + 5)

sum = 0
for ai in a:
    s[ai] += 1; sum += ai;

for i in range(q):
    b, c = map(int, input().split())
    cnt = s[b]; s[b] = 0; s[c] += cnt;
    sum += (c - b) * cnt
    print(sum)
