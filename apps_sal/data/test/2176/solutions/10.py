def increasing(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i + 1][0] < arr[i][0] or arr[i + 1][1] < arr[i][1]:
            return False
    return True


def getFacts(n, mod):
    facts = [1] * n
    for i in range(1, n):
        facts[i] = facts[i - 1] * i
        facts[i] %= mod
    return facts


def solve(arr1, arr2, n, mod):
    facts = getFacts(4 * 10 ** 5 + 1, mod)
    total = facts[n]
    dist1 = {}
    for i in arr1:
        if i[0] not in list(dist1.keys()):
            dist1[i[0]] = 1
        else:
            dist1[i[0]] += 1
    dist2 = {}
    for i in arr2:
        if i[0] not in list(dist2.keys()):
            dist2[i[0]] = 1
        else:
            dist2[i[0]] += 1
    count = 1
    for i in dist1:
        count *= facts[dist1[i]]
        count = count % mod
    total -= count
    count = 1
    for i in dist2:
        count *= facts[dist2[i]]
        count = count % mod
    total -= count
    arr1.sort()
    if increasing(arr1):
        count = 1
    else:
        count = 0
    dist3 = {}
    for i in arr1:
        if i not in list(dist3.keys()):
            dist3[i] = 1
        else:
            dist3[i] += 1
    for i in dist3:
        count *= facts[dist3[i]]
        count = count % mod
    total += count
    total = total % mod
    print(total)


def main():
    mod = 998244353
    n = int(input())
    first = []
    second = []
    for i in range(n):
        (a, b) = list(map(int, input().split()))
        first.append((a, b))
        second.append((b, a))
    solve(first, second, n, mod)


main()
