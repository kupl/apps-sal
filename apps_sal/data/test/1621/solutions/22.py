def readln(): return tuple(map(int, input().split()))


s = input()
k, = readln()
w = readln()
ans = sum([(i + 1) * w[ord(c) - ord('a')] for i, c in enumerate(s)])
print(ans + max(w) * (2 * len(s) + k + 1) * k // 2)
