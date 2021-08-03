t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    x = [i for i in range(n) if s[i] == '1']
    if len(x) == 0:
        print(n)
    else:
        print(max(max(i + 1 + i + 1, n - i + n - i) for i in x))
