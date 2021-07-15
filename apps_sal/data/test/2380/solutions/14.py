import heapq

n, m = list(map(int, input().split()))
cards = list(map(int, input().split()))
cards.sort()

queries = []
for i in range(m):
    q = list(map(int, input().split()))
    queries.append(q)
queries.sort(key=lambda x: x[1])
queries.reverse()

ans = 0
pos = 0
for q in queries:
    b, c = q
    if cards[min(pos+b-1, n-1)] < c:
        # print('a')
        pos = pos + b
        ans += c * (b - max(0, pos-n))
        if pos >= n:
            break
    else:
        for i in range(b):
            if cards[pos+i] < c:
                # print('b')
                ans += c
            else:
                # print('c')
                pos += i
                for j in range(pos, n):
                    ans += cards[j]

                pos = n
                break
        break

if pos < n:
    for j in range(pos, n):
        ans += cards[j]

print(ans)


