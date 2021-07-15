T = int(input())
for _ in range(T):
    n, a, b = map(int, input().split())
    s = list(map(int, input()))
    if 1 not in s:
        print(a*n + b*(n+1))
        continue
    min_lower_length = 2*a/b + 1
    start = 0
    while s[start] == 0:
        start += 1
    end = n-1
    while s[end] == 0:
        end -= 1
    cost = (n+2)*a + (n+1)*b + (end-start+2)*b
    c = 0
    for i in range(start, end+1):
        if s[i] == 0:
            c += 1
        else:
            if c>=min_lower_length:
                cost += 2*a - (c-1)*b
            c = 0
    print(cost)
