import sys
input = sys.stdin.readline

n, k = map(int, input().split())
h_list = []

for _ in range(n):
    h_list.append(int(input()))

sort_h_list = sorted(h_list)

L_index = 0
R_index = 0
L_value = sort_h_list[0]
R_value = sort_h_list[0]
count = 0
ans = 10**9

while (R_index < n):
    if (count < k):
        count += 1
        R_value = sort_h_list[R_index]
        if count == k:
            ans = min(ans, R_value - L_value)
        R_index += 1

    else:
        count -= 1
        L_index += 1
        L_value = sort_h_list[L_index]

print(ans)
