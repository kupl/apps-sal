n, m = list(map(int, input().split()))
s_li = []
c_li = []
for _ in range(m):
    s_in, c_in = list(map(int, input().split()))
    s_li.append(s_in - 1)
    c_li.append(c_in)

if n == 1:
    ans = ["0"]
else:
    ans = list(str(10**(n - 1)))

check = [0] * n

for s, c in zip(s_li, c_li):
    if check[s] == 0:
        ans[s] = str(c)
        check[s] = 1
    else:
        if ans[s] == str(c):
            continue
        print((-1))
        return

if n > 1 and ans[0] == "0":
    print((-1))
else:
    print(("".join(ans)))
