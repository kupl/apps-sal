s = int(input())
ans = 1
s_st = set()
while s not in s_st:
    s_st.add(s)
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
    ans += 1
print(ans)
