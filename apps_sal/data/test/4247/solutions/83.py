
n = int(input())
l_n = list(map(int, input().split()))
ans_count = 0

for i in range(n - 2):
    a = l_n[i]
    b = l_n[i + 1]
    c = l_n[i + 2]
    if a <= b <= c or c <= b <= a:
        ans_count += 1

print(ans_count)
