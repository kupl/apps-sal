n_list = list(input())

n = [int(i) for i in n_list]

ans = str(n[0] + 1) * 3

if n[0] > n[1]:
    ans = str(n[0]) * 3

elif n[0] == n[1]:
    if n[1] >= n[2]:
        ans = str(n[0]) * 3

print(ans)
