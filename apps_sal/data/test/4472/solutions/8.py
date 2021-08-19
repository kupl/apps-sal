n = int(input())
st1 = list(input())
st2 = list(input())
ans = 0
for i in range(n // 2 + n % 2):
    if i == n - i - 1:
        if st1[i] != st2[i]:
            ans += 1
        break
    if st2[i] == st2[n - i - 1]:
        if st1[i] != st1[n - i - 1]:
            ans += 1
    else:
        if st1[i] != st2[i] and st1[n - i - 1] != st2[i]:
            ans += 1
        if st1[i] != st2[n - i - 1] and st1[n - i - 1] != st2[n - i - 1]:
            ans += 1
print(ans)
