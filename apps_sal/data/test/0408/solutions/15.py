input_str = input()
n, k = int(input_str.split()[0]), int(input_str.split()[1])
teams = 0
if k >= n * 2:
    print(n)
elif n >= k * 2:
    print(k)
else:
    while n + k >= 3 and k > 0 and n > 0:
        teams += 1
        if n < k:
            n -= 1
            k -= 2
        else:
            n -= 2
            k -= 1
    print(teams)
