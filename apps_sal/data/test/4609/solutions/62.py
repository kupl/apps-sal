n = int(input())
count_dict = {}
for i in range(n):
    new = int(input())
    if new in count_dict:
        count_dict[new] += 1
    else:
        count_dict[new] = 1
ans = 0
for i in count_dict.values():
    if i % 2 == 1:
        ans += 1
print(ans)
