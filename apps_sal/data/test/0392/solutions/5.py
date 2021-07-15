n = int(input())

for_ans = set()
i = 2

while i <= n ** 0.5:
    if n % i == 0:
        for_ans.add(i)
        n //= i
    else:
        i += 1

ans = 1
for_ans.add(n)

for e in for_ans:
    ans *= e

print(ans)
