def f(s, n):
    ans = ''
    for c in s:
        ans += chr(ord('A') + (ord(c)-ord('A')+n) % 26)
    return ans

N = int(input())
S = input()
print(f(S, N))
