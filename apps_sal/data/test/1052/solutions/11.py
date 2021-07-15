n, k = map(int, input().split())
facts = [1]
for i in range(1, n + 1):
    facts.append(i * facts[i - 1])
ans = facts[n]
if k >= 1:
    ans = 1
if k >= 2:
    ans += facts[n] // facts[n - 2] //facts[2]
if k >= 3:
    ans += 2 *facts[n] // facts[n - 3] // facts[3]
if k == 4:
    ans+= 9 *facts[n] // facts[n - 4] // facts[4]
print(ans)
