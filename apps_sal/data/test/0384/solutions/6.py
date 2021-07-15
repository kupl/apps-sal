n = int(input())
s = input()
curr_b = 0
ans = []
for i in range(n):
    if s[i] == 'B':
        curr_b += 1
        if i == n - 1:
            ans.append(curr_b)
    else:
        if i > 0 and s[i - 1] == 'B':
            ans.append(curr_b)
        curr_b = 0
print(len(ans))
for i in ans:
    print(i, end = " ")
