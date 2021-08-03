def solve():
    a, k = list(map(int, input().split()))
    seen = set()
    items = [a]
    for i in range(k - 1):
        last = items[-1]
        min_dig = int(min(str(last)))
        max_dig = int(max(str(last)))
        nw = last + min_dig * max_dig
        items.append(nw)
        if '0' in str(items):
            break
    print(items[-1])


for i in range(int(input())):
    solve()
