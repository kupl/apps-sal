from functools import reduce
N = int(input())
S = input()
ans = [chr(ord('A') + (ord(s) + N - ord('A')) % 26) for s in S]
ans = reduce(lambda x, y: x + y, ans)
print(ans)
