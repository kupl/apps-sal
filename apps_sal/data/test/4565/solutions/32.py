n = int(input())
s = input()
e = s.count('E')
w = s.count('W')
ans = 1000000
e_counter = 0
w_counter = 0
for i in range(len(s)):
    if s[i] == 'E':
        e_counter += 1
    else:
        w_counter += 1
    d = w_counter
    if s[i] == 'W':
        d -= 1
    ans1 = d + (e - e_counter)
    ans = min(ans1, ans)
print(ans)
