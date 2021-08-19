def main():
    (n, m) = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    sums = []
    visited = set()
    for i in range(1, n + 1):
        if i not in visited:
            total = 0
            for j in range(i, n + 1, m):
                visited.add(j)
                total += arr[j - 1]
            sums.append([i, total])
    ans = []
    total = 0
    count = 0
    day = 1
    for i in arr:
        total += i * day
        count += 1
        if count % m == 0:
            day += 1
            count = 0
    ans.append(total)
    index = 0
    for i in range(n - 1):
        total -= sums[index][1]
        curr = arr[sums[index][0] - 1]
        sums[index][1] -= curr
        sums[index][0] += m
        ans.append(total)
        index += 1
        if index == len(sums):
            index = 0
    ans.reverse()
    for i in ans:
        print(i, end=' ')


main()
