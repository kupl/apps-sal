def norm(s):
    return [(x + 10 - s[0]) % 10 for x in s]

n, = list(map(int, input().split()))
s = input().strip()
s = [int(x) for x in s]
print("".join(map(str, min([norm(s[j:] + s[:j]) for j in range(n)]))))

