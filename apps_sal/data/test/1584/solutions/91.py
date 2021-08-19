N = int(input())
l = list(map(int, input().split()))
l.sort()
ans = 0
max = l[N - 1]
tc = N
st = [j + 1 for j in range(N - 1)]
for i in range(N - 2):
    if l[i] + l[i + 1] > max:
        k = N - i - 1
        ans += (k - 1) * k * (k + 1) // 6
        break
    for j in range(i + 1, N - 1):
        if j == tc:
            ans += tp
            break
        s = l[i] + l[j]
        if s <= l[j + 1]:
            continue
        if s > max:
            tc = j
            tp = (N - j - 1) * (N - j) // 2
            ans += tp
            break
        start = st[j]
        if s <= l[start]:
            ans += start - j - 1
            continue
        end = N
        while start != end:
            center = (start + end) // 2
            if s <= l[center]:
                end = center
            else:
                start = center + 1
        st[j] = end
        ans += end - j - 1
print(ans)
