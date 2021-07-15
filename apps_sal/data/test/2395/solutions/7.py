n = int(input())
for _ in range(n):
    s = input()
    p = len(s)
    if all(c == s[0] for c in s):
        print(s)
    else:
        print('01' * p)
