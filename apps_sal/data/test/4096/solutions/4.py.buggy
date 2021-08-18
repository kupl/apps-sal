n, m = map(int, input().split())
a = input().split()
a = [int(i) for i in a]

s = sum(a)
if s < m:
    print(-1)
elif s == m:
    print(n)
else:
    a.sort(reverse=True)
    # print(a)
    for day in range(1, n + 1):
        coffee = [0 for _ in range(day)]
        paper = [0 for _ in range(day)]
        i = 0
        while i < n:
            if a[i] - coffee[i % day] > 0:
                paper[i % day] += a[i] - coffee[i % day]
                coffee[i % day] += 1
            i += 1
        # print(coffee, paper)
        if sum(paper) >= m:
            print(day)
            return
