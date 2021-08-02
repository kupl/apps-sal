n = int(input())

p = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
ans = 1;
ind = 1

for i in p:
    if c[i - 1] != c[ind]:
        ans += 1;
    ind += 1

print(ans)
