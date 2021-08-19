q = int(input())
for _ in range(q):
    n = int(input())
    s = input()
    min_pos = -1
    max_pos = -1
    for i in range(n):
        if s[i] == '1':
            max_pos = i
    for i in range(n)[::-1]:
        if s[i] == '1':
            min_pos = i
    if min_pos == -1:
        print(n)
    else:
        print(max(2 * (max_pos + 1), 2 * (n - min_pos)))
