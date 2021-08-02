n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
has = [0] * (n)
ans = []
for i in range(n):
    has[b[i]] += 1
child = [i for i in range(1, n)] + [0]
for i in a:
    no = (n - i) % n
    while has[no] == 0:
        if has[child[no]] == 0:
            child[no] = child[child[no]]
        no = child[no]
    has[no % n] -= 1
    ans.append((no % n + i) % n)
print(*ans)
