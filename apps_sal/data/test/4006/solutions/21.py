def f(x):
    return str(n + 1).rstrip('0')


n = int(input())
s = set()
while n not in s:
    s.add(n)
    n = int(f(n))
print(len(s))
