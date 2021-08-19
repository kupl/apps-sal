(n, m, r) = [int(item) for item in input().split()]
s = [int(item) for item in input().split()]
b = [int(item) for item in input().split()]
x = r // min(s)
print(max(r, x * max(b) + r % min(s)))
