n, m = list(map(int, input().split()))
s = input()
p = [chr(i) for i in range(97, 97 + 26)]
for i in range(m):
    a, b = input().split()
    for i in range(26):
        if p[i] == a:
            p[i] = b
        elif p[i] == b:
            p[i] = a
print("".join([p[ord(x) - 97] for x in s]))
