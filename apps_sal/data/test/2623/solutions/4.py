t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    s = input()
    chars = sorted([c for c in s])
    if chars[k-1] > chars[0]:
        print(chars[k-1])
    elif chars[0] == chars[n-1]:
        print(''.join([chars[0]] * ((n + k - 1) // k)))
    elif chars[k] != chars[0] and chars[k] == chars[n-1]:
        print(''.join([chars[0]] + [chars[k]] * ((n - 1) // k)))
    else:
        print(''.join(chars[k-1:]))

