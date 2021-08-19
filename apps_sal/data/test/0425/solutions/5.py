(n, p) = map(int, input().split())
min_ans = -1
for i in range(1, 10000):
    nn = n
    nn -= i * p
    if nn > 0:
        st = bin(nn)[2:]
        if st.count('1') <= i and nn >= i:
            min_ans = i
            break
print(min_ans)
