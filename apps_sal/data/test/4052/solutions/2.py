n = int(input())
st1 = list(input())
st2 = list(input())
ans = 0
anslist = []
for i in range(n):
    if st1[i] != st2[i]:
        f = True
        for j in range(i + 1, n):
            if st1[j] == st2[i]:
                ans += j - i
                anslist += [k + 1 for k in reversed(range(i, j))]
                f = False
                st1 = st1[:i] + st1[j:j + 1] + st1[i:j] + st1[j + 1:]
                break
        if f:
            print(-1)
            quit()
print(ans)
for i in anslist:
    print(i, end=" ")
print()
