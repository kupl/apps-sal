n = int(input())
a = list(map(int, input().split()))
check = [0] * 100100
for x in a:
    check[x] += 1
q = int(input())
ans = sum(a)
for i in range(q):
    b, c = list(map(int, input().split()))
    ans += (c - b) * check[b]
    check[c] += check[b]
    check[b] = 0
    print(ans)
