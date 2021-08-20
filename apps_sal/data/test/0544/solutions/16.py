num_cases = int(input())
for case in range(num_cases):
    n = int(input())
    s = input()
    solution = 'YES'
    for i in range(n // 2):
        d = abs(ord(s[i]) - ord(s[n - i - 1]))
        if not d == 0 and (not d == 2):
            solution = 'NO'
            break
    print(solution)
