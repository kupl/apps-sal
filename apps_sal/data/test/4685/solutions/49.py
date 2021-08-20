num_list = list(map(int, input().split()))
k = int(input())
max = 0
index = -1
for i in num_list:
    if max < i:
        max = i
        index = num_list.index(i)
change = max * 2 ** k
num_list[index] = change
ans = 0
for j in num_list:
    ans += j
print(ans)
