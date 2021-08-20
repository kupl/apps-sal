def joy(f: int, t: int, k: int) -> int:
    return f - (t - k) if t > k else f


(n, k) = map(int, input().split())
joys = [0] * n
for i in range(n):
    (f, t) = map(int, input().split())
    joys[i] = joy(f, t, k)
print(max(joys))
