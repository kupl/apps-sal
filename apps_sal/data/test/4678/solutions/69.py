from sys import stdin
N = int(stdin.readline().rstrip())
A = [int(_) for _ in stdin.readline().rstrip().split()]
ans, tmp_max = 0, 0
for a in A:
    if a > tmp_max:
        tmp_max = a
    else:
        ans += (tmp_max - a)
print(ans)
