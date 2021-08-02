t = int(input())
for tc in range(t):
    n = int(input())
    s = input()
    n = -1
    for c in s:
        if n >= 0:
            n += 1
        elif n == -1 and c == '8':
            n = 0
    print("YES" if n >= 10 else "NO")
