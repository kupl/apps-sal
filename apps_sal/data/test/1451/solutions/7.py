3

n, k = list(map(int, input().split()))
a = input().split()

tmp = [len([1 for c in list(v) if c in ('4', '7')]) for v in a]
print(len([1 for _ in tmp if _ <= k]))
