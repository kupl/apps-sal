s = input()
a = list(map(int, input().split()))
ans = 0
mean = round(sum(a) / len(a))

for i in a:
    p = (i - mean)**2
    ans += p

print(ans)
