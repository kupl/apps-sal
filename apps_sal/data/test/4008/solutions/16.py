n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = [0] * (5001)
for i in a:
    d[i] += 1
for i in range(1, 5001):
    if(d[i] > k):
        print("NO")
        break
else:
    done = []
    for i in range(5001):
        done.append(set())
    for i in range(k):
        done[a[i]].add(i + 1)
        a[i] = i + 1
    for i in range(k, n):
        for j in range(1, k + 1):
            if(j not in done[a[i]]):
                done[a[i]].add(j)
                a[i] = j
                break
    print("YES")
    print(*a)
