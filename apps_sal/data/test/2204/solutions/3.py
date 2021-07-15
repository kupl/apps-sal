import bisect
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    flowers = []
    flowers_a = []
    max_b = 0
    for i in range(m):
        a, b = list(map(int, input().split()))
        flowers.append((a, b))
    
    flowers.sort()
    flowers_b = []
    for i in range(m):
        flowers_a.append(flowers[i][0])
        flowers_b.append(flowers[i][1])
    
    val = 0
    prefix_sum = [0]
    for x in flowers_a:
        prefix_sum.append(prefix_sum[-1] + x)
    for i in range(m):
        idx = bisect.bisect_left(flowers_a, flowers_b[i])
        options = m - idx
        if options >= n:
            temp = prefix_sum[-1] - prefix_sum[-n - 1]
            val = max(val, temp)
            continue
        else:
            temp = prefix_sum[-1] - prefix_sum[-options - 1]
            remaining = n - options
            if idx <= i:
                temp += flowers_b[i] * remaining
            else:
                temp += flowers_a[i] + flowers_b[i] * (remaining - 1)
            
            val = max(val, temp)
                

    print(val)
    
    if _ != t - 1:
        blank_line = input()

