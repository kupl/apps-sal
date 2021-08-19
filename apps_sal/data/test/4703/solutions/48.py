S = input()
len_S = len(S)
ans = 0
left = 0
is_plus = [0] * (len_S - 1)
for i in range(2 ** (len_S - 1)):
    left = 0
    for j in range(len_S - 1):
        (i, mod) = divmod(i, 2)
        if mod == 1:
            ans += int(S[left:j + 1])
            left = j + 1
    ans += int(S[left:len_S])
print(ans)
