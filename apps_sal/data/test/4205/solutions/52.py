n = int(input())
p_list = [int(i) for i in input().split()]

np_list = sorted(p_list)

count = 0
for i in range(n):
    if p_list[i] != np_list[i]:
        count += 1

if count == 2 or count == 0:
    ans = "YES"
else:
    ans = "NO"

print(ans)
