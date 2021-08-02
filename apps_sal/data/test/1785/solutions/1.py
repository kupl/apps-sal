import sys
# sys.stdin = open('in.txt')
R = lambda: map(int, input().split())

n = int(input())
s = input()

ca = s.count('A')
cg = s.count('G')
cc = s.count('C')
ct = s.count('T')
mx = max(ca, cg, cc, ct)

sum = (ca == mx) + (cg == mx) + (cc == mx) + (ct == mx)

ans = 1

for i in range(n):
    ans = (ans * sum) % 1000000007

print(ans)
